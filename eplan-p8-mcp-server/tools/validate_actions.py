"""
Cross-check the MCP action wrappers against the official EPLAN P8 docs RAG.

For every function in mcp_server/api/actions/*.py it extracts:
  - the EPLAN action name declared in the docstring ("Action: <Name>")
  - the parameter keys passed to _build_action(...)

and then queries the remote RAG (https://rag2026.covaga.xyz/search) to verify:
  1. the action name exists in the official documentation
  2. each parameter key appears in the matched documentation page

Usage:
    python tools/validate_actions.py [--top-k 5] [--out report.md]

No third-party dependencies (urllib only).
"""

import argparse
import ast
import json
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

RAG_URL = "https://rag2026.covaga.xyz/search"
ACTIONS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "mcp_server", "api", "actions",
)
ACTION_RE = re.compile(r"Action:\s*([A-Za-z0-9_]+)")

# Parameter keys that are wrapper-internal or too generic to validate
IGNORED_PARAMS = {"TYPE"}


def extract_wrappers():
    """Parse every action module and return [(module, func, action, params)]."""
    wrappers = []
    for fname in sorted(os.listdir(ACTIONS_DIR)):
        if not fname.endswith(".py") or fname.startswith("_"):
            continue
        path = os.path.join(ACTIONS_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=path)
        for node in tree.body:
            if not isinstance(node, ast.FunctionDef) or node.name.startswith("_"):
                continue
            doc = ast.get_docstring(node) or ""
            m = ACTION_RE.search(doc)
            action = m.group(1) if m else None

            params = set()
            for call in ast.walk(node):
                if (
                    isinstance(call, ast.Call)
                    and isinstance(call.func, ast.Name)
                    and call.func.id == "_build_action"
                ):
                    for kw in call.keywords:
                        if kw.arg and kw.arg not in IGNORED_PARAMS:
                            params.add(kw.arg)
            wrappers.append((fname[:-3], node.name, action, sorted(params)))
    return wrappers


def rag_search(query, top_k):
    body = json.dumps({"query": query, "topK": top_k}).encode("utf-8")
    req = urllib.request.Request(
        RAG_URL,
        data=body,
        # Cloudflare rejects the default python-urllib User-Agent with a 403
        headers={"Content-Type": "application/json", "User-Agent": "curl/8"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def check_action(action, params, top_k):
    """Return a result dict for one EPLAN action name."""
    # Two query phrasings: semantic search sometimes misses the exact page
    # with one of them (e.g. very generic names like "check" or "edit").
    queries = [f"{action} action parameters", action]
    matches = []
    seen_ids = set()
    word = re.compile(rf"\b{re.escape(action)}\b", re.IGNORECASE)
    try:
        for q in queries:
            data = rag_search(q, top_k)
            for r in data.get("results", []):
                if r.get("id") in seen_ids:
                    continue
                seen_ids.add(r.get("id"))
                if word.search(r.get("title", "")) or word.search(r.get("content", "")):
                    matches.append(r)
    except Exception as e:
        return {"action": action, "status": "error", "detail": str(e)}

    if not matches:
        return {"action": action, "status": "not_found",
                "detail": "no doc page mentions this action (undocumented internal action or index gap)"}

    # A parameter counts as documented if it appears in ANY matching chunk
    # (RAG chunks are truncated, so a single chunk rarely holds the full page).
    corpus = "\n".join(m.get("content", "") + "\n" + m.get("title", "") for m in matches)
    missing = [
        p for p in params
        if not re.search(rf"\b{re.escape(p)}\b", corpus, re.IGNORECASE)
    ]
    best = matches[0]
    return {
        "action": action,
        "status": "ok" if not missing else "params_missing",
        "detail": f"params not seen in docs: {missing}" if missing else "",
        "doc": best.get("source_url", best.get("title", "")),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "action_validation_report.md"))
    args = parser.parse_args()

    wrappers = extract_wrappers()
    scripted = [(m, f) for m, f, a, _ in wrappers if a is None for _ in [0]]
    declared = {}
    for module, func, action, params in wrappers:
        if action:
            entry = declared.setdefault(action, {"params": set(), "funcs": []})
            entry["params"].update(params)
            entry["funcs"].append(f"{module}.{func}")

    print(f"Wrappers: {len(wrappers)} functions, {len(declared)} unique EPLAN actions, "
          f"{len(scripted)} scripted/no-action (skipped)")

    results = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {
            pool.submit(check_action, action, sorted(info["params"]), args.top_k): action
            for action, info in declared.items()
        }
        done = 0
        for fut in as_completed(futures):
            res = fut.result()
            results[res["action"]] = res
            done += 1
            if done % 20 == 0:
                print(f"  {done}/{len(futures)} checked...")

    order = {"not_found": 0, "error": 1, "params_missing": 2, "ok": 3}
    rows = sorted(results.values(), key=lambda r: (order[r["status"]], r["action"]))
    counts = {s: sum(1 for r in rows if r["status"] == s) for s in order}

    lines = [
        "# EPLAN Action Validation Report",
        "",
        f"Checked **{len(rows)}** unique EPLAN actions against the official docs RAG (`{RAG_URL}`).",
        "",
        f"- OK: {counts['ok']}",
        f"- Action found but some parameter names not in the doc page: {counts['params_missing']}",
        f"- Action NOT found in docs: {counts['not_found']}",
        f"- Request errors: {counts['error']}",
        "",
        "| Status | Action | Wrapper(s) | Detail |",
        "|--------|--------|------------|--------|",
    ]
    icon = {"ok": "OK", "params_missing": "WARN", "not_found": "NOT FOUND", "error": "ERROR"}
    for r in rows:
        funcs = ", ".join(declared[r["action"]]["funcs"])
        doc = r.get("doc", "")
        detail = r.get("detail", "")
        if doc:
            detail = f"{detail} [doc]({doc})" if detail else f"[doc]({doc})"
        lines.append(f"| {icon[r['status']]} | `{r['action']}` | `{funcs}` | {detail} |")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\nReport written to {args.out}")
    print(f"OK={counts['ok']}  WARN(params)={counts['params_missing']}  "
          f"NOT_FOUND={counts['not_found']}  ERROR={counts['error']}")
    return 0 if counts["not_found"] == 0 and counts["error"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
