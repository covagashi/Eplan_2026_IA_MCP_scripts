---
name: eplan-development
description: Develop EPLAN Electric P8 scripts, API extensions, and remote-control applications. Use when writing C# scripts for EPLAN (actions, event handlers, ribbon), accessing the EPLAN API (parts database, projects, pages), building external apps that drive EPLAN via Remote Client, or debugging EPLAN automation issues (blocking, threading, dispose). Covers EPLAN 2022–2025.
---

# EPLAN Electric P8 Development

Comprehensive guide for developing with EPLAN Electric P8: scripting (C#), the EPLAN API, and remote automation. Distilled from working production code and curated examples.

## The three development models

| Model | Runs | License | Use for |
|---|---|---|---|
| **Scripting** | Inside EPLAN (compiled on load, C# subset) | None extra | Automating actions, UI additions (ribbon), event hooks, file exports |
| **API extension** | Inside EPLAN (compiled DLL) or offline app | API license | Deep data access: parts DB, project object model, pages, properties |
| **Remote Client** | External process (WPF/console) driving a running EPLAN | RemoteClient DLLs | Orchestration apps, headless build pipelines, Cogineer generation |

Note: scripts CAN use some API namespaces (e.g. `Eplan.EplApi.MasterData` for the parts database) directly from a `[Start]` method — see `references/api-data-access.md`.

## Reference files — read the one that matches the task

- **`references/script-basics.md`** — Script structure, entry-point attributes (`[Start]`, `[DeclareAction]`, `[DeclareEventHandler]`, `[DeclareRegister]`), deployment, scripting limitations.
- **`references/actions-reference.md`** — Executing actions with `CommandLineInterpreter` + `ActionCallingContext`; catalog of common actions (backup, export PDF, reports, labels, edit, selectionset…) with their parameters.
- **`references/core-classes.md`** — `Progress`, `Decider`, `PathMap` variables, `Settings`, `MultiLangString`, ribbon/context menus, `QuietModeStep`, system messages (`BaseException`, `SysMessagesCollection`).
- **`references/api-data-access.md`** — Parts database (`MDPartsManagement`), part properties, user-defined properties, multilanguage string parsing, resolving `$(MD_DOCUMENTS)`-style paths.
- **`references/remoting.md`** — `EplanRemoteClient`: server discovery, dynamic ports, headless launch, version gotchas (2023 vs 2025), executing actions and scripts remotely, Cogineer generation from Excel.
- **`references/pitfalls.md`** — CRITICAL: the command-blocking issue (message loop / monitor thread), `using`/`Dispose` discipline, sequential execution model, error-handling rules.
- **`references/integration-patterns.md`** — Connecting EPLAN to the outside: HTTP servers, SignalR real-time messaging, forwarding EPLAN system errors to external services.

## When you don't know something: query the RAG

A semantic search service indexes the full EPLAN P8 documentation (API reference, user guide, hidden/undocumented actions — ~57k vectors). **Always query it before guessing** action names, parameters, or API signatures:

```bash
curl -X POST https://rag2026.covaga.xyz/search \
  -H "Content-Type: application/json" \
  -d '{"query": "export project to PDF parameters", "topK": 5}'
```

- `POST /search` — body `{"query": "...", "topK": N}` (public, no auth)
- `GET /stats` — index statistics; `GET /health` — health check

Use natural-language queries in English ("action to renumber devices", "PagePropertyList page type values"). Prefer several narrow queries over one broad one.

## Golden rules (violating these causes real production failures)

1. **EPLAN actions are pseudo-asynchronous.** After `oCLI.Execute(...)` in an external/long-running context, code can hang forever without an active message loop. See `references/pitfalls.md` before writing any multi-step automation.
2. **Dispose everything.** `ActionCallingContext`, `EplanRemoteClient`, temp clients — wrap in `using` or dispose in `finally`.
3. **Operations are sequential.** Each EPLAN action must fully finish before the next; never fire actions in parallel against one instance.
4. **Never use empty `catch {}`.** Log with `BaseException(msg, MessageLevel.X).FixMessage()` (inside EPLAN) or a logger (outside).
5. **EPLAN 2025 remoting requires "Remote Client Access"** enabled in EPLAN options; transport is gRPC (default port 49152, dynamic). In 2023 it was on by default.
6. **Target .NET Framework 4.8.1** for EPLAN 2025 API/RemoteClient work; reference DLLs from `C:\Program Files\EPLAN\Platform\<version>\Bin\`.
7. **Verify action names/parameters against the RAG** — many are undocumented and case-sensitive.
