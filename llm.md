# LLM Operating Guide — EPLAN AI Automation Toolkit

This file tells you (the LLM) what this toolkit lets you **do** and **configure**.
It assumes you are connected through one or more of the MCP servers in this repo.

---

## 1. What you are connected to

There are up to **three MCP servers**, each a different capability:

| MCP server | Kind | What it lets you do |
|------------|------|---------------------|
| `eplan` (local) | Action server | **Control a running EPLAN Electric P8 instance** — open/close projects, export, import, reports, checks, renumber, parts DB, settings, run C# scripts, etc. |
| `eplan-rag` (remote) | Knowledge | **Look up the EPLAN P8 API** (actions, classes, properties, parameters) via semantic search. |
| `eecpro-rag` (remote) | Knowledge | **Look up the EPLAN EEC Pro 2026** documentation via semantic search. |

If `eplan-rag` is not connected, you can still query the P8 docs over REST:
`POST https://rag2026.covaga.xyz/search` with body `{"query": "...", "topK": 5}`.
Use this whenever you are unsure of an exact action name or parameter — **do not
guess EPLAN action parameters**.

---

## 2. The local `eplan` action server

It exposes **304 tools**:

- **6 connection/utility tools** (version-agnostic): `eplan_servers`,
  `eplan_connect`, `eplan_status`, `eplan_ping`, `eplan_test`, `eplan_disconnect`.
- **149 EPLAN actions × 2 execution modes** → `eplan_v1_<action>` and
  `eplan_v2_<action>`.

Each tool already carries its own description and parameter schema (generated
from the Python docstring + type hints). **Read the tool's own description before
calling it** — this guide is the map, the tool schemas are the territory.

### V1 vs V2 — which to use

- **`eplan_v2_*` (DEFAULT, recommended).** The action runs inside a C# script in
  EPLAN's process under `QuietMode` (no dialogs). It is silent, safe for
  unattended/batch use, and returns values EPLAN wrote back to the calling
  context (e.g. `PROJECT`, `PAGES`). Prefer this unless you have a reason not to.
- **`eplan_v1_*`.** Direct execution via the Remote API. Faster, but EPLAN may
  pop up dialogs that block until a human responds. Use only for simple or
  intentionally interactive tasks.

### Result shape

Tools return JSON. V2 actions typically return:

```json
{ "success": true, "parameters": { "PROJECT": "C:\\...\\Proj.elk" } }
```

`success: false` with a `message`/`error` means the EPLAN action itself failed —
read the message; it usually points at a bad parameter or a missing precondition
(e.g. no project open).

---

## 3. Standard workflow

1. **Check / connect first.** Call `eplan_status` (or `eplan_servers` →
   `eplan_connect`). Almost every action needs an open connection. Port is
   auto-detected; if `eplan_servers` returns `[]` the connection still works via
   the default port (49152) — that empty list is a known limitation, not a
   failure.
2. **Pick the project context.** Most actions take an optional `project_name`. If
   omitted, EPLAN uses the **currently selected/open** project. Use
   `eplan_v2_get_current_project` to confirm what that is.
3. **Prefer V2.** Call `eplan_v2_<action>` with the parameters from the tool
   schema.
4. **Verify unknowns via the RAG** before constructing raw actions or custom
   scripts.
5. **Report results** from the returned JSON honestly (including `success: false`).

---

## 4. What you can DO (capability map)

All of these exist as both `eplan_v1_*` and `eplan_v2_*`:

- **Projects:** open, close, get current, compress, synchronize, upgrade, set
  language, switch type, project management tasks.
- **Backup / restore:** projects and master data.
- **Export:** PDF (project/pages), DXF/DWG (project/pages, by scheme), graphics
  (PNG/TIF/…), PXF/EPJ, 3D.
- **Import:** PXF projects, DXF/DWG into pages or as macros, PDF comments, 3D.
- **Print:** project or pages.
- **Check / verify:** project, pages, parts (with verification schemes).
- **Generate:** connections, cables.
- **Reports / evaluations:** update reports, model views, copper unfolds,
  drilling views.
- **Search:** devices, texts, all properties, page data, project data.
- **Navigation / editing:** open page, go to device, open layout space, close
  pages, get selected pages, page/macro preview, navigate to EEC.
- **Renumber:** devices, pages, cables, terminals, connections.
- **Translate:** translate project, export missing translations, remove language.
- **Device lists, labels, graphical layers, macros.**
- **Settings & properties:** import/export settings, set settings, get/set
  project / page / object properties, user properties.
- **Parts:** export/import parts lists, part selection, data source, full parts
  management API export/import.
- **PLC:** bus data export/import via converters.
- **Workspace:** open/save/clean (needs the EPLAN GUI/mainframe).
- **Data exchange:** connections/functions/pages export for external editing,
  data-configuration import/export, potential/pipeline definitions, subprojects,
  master data operations.
- **Cabinet / 3D:** cabinet weight, segment filling, topology, pre-planning data,
  segment templates.
- **Production:** NC data, production wiring.
- **Ribbon & add-ons:** export/import ribbon bar, load API module, register/
  unregister add-on, and `execute_raw_action` for any action not wrapped.
- **Scripted advanced APIs (`eplan_v2_*` only, run as C#):** direct **parts
  database** queries (`parts_db_*`), **typed settings** get/set
  (`settings_get/set_string|bool|int|double`), **PathMap** variable substitution,
  and `execute_custom_script` to run arbitrary C# inside EPLAN.

### Escape hatches

- `eplan_v2_execute_raw_action("ActionName /PARAM:value ...")` — run any EPLAN
  action string directly (still wrapped in QuietMode). Use after confirming the
  syntax with the RAG.
- `eplan_v2_execute_custom_script(<C# code>)` — run a full C# script with access
  to `Eplan.EplApi.*`. Write results to `{{RESULT_PATH}}` as JSON.

---

## 5. What you can CONFIGURE

- **Target EPLAN version** (e.g. 2025 → 2026): edit `TARGET_VERSION` in **4
  files** — `server.py`, `api/v1/actions/_base.py`, `api/v2/actions/_base.py`,
  and the default `target_version` in `eplan_connection.py`. Then restart.
- **Add a new action / tool:** implement a function in
  `api/v2/actions/<module>.py` (and/or V1), export it in that package's
  `__init__.py` `__all__`, restart. It auto-registers as `eplan_v2_<name>`. The
  docstring + type hints become the tool description and schema you will see.
- **EPLAN settings at runtime:** via `eplan_v2_set_setting` /
  `eplan_v2_set_project_setting` (action params `set`/`value`/`index`) or the
  typed `eplan_v2_settings_set_*` scripted tools.
- **The MCP registration itself:** `claude mcp add eplan -- python .../server.py`.

---

## 6. Caveats & gotchas

- **Connect before acting.** Unconnected calls return a "Not connected" error.
- **`project_name` is optional** — omitting it uses the selected project. Pass the
  full `.elk` path to be explicit. Windows paths must be escaped (`\\`) or use `/`.
- **GUI-only actions** behave poorly headless/under QuietMode: `redraw_ged`
  (returns FALSE in QuietMode) and the `workspace` actions (need a mainframe).
- **Property actions on project/page** (`get/set_project_property`,
  `get/set_page_property`) act on the **current project / selected page(s)** and
  use `PropertyId`/`PropertyIndex`/`PropertyValue` — they do not take a project
  or page name.
- **`selectionset`** valid `TYPE` values are `PROJECT`, `PROJECTS`, `PAGES`,
  `LAYOUTSPACES` only.
- **Don't invent parameters.** When unsure, query the RAG (`rag2026.covaga.xyz`)
  for the authoritative action page.

---

## 7. Safety — confirm before destructive actions

Treat these as outward/irreversible and **confirm with the user first** unless
explicitly authorized: deleting pages or device/parts lists, closing a project
with unsaved changes, renumbering (devices/pages/cables/terminals/connections),
restore/backup overwrites, settings changes, `set_*_property`, raw actions, and
custom C# scripts. Read-only actions (status, search, get current project,
exports to new files, parts DB queries) are safe to run as needed.
