# EPLAN MCP Server

Remote control of **EPLAN Electric P8** from an LLM (e.g. Claude) via MCP (Model Context Protocol).

The server connects to a running EPLAN instance through the EPLAN Remote Client API
(pythonnet / CLR) and exposes **156 MCP tools**: 7 connection/utility tools plus
**149 EPLAN actions** (`eplan_*`).

The EPLAN version is **auto-detected** (newest installed under
`C:\Program Files\EPLAN\Platform`); the LLM can override it per session via
`eplan_connect(version=...)`.

Every action is wrapped in a dynamically generated C# script executed **inside
EPLAN's process** under `QuietMode` (`QuietModes.ShowNoDialogs`). Completely
silent, prevents blocking dialogs, and reads return values back from the
`ActionCallingContext` — safe for batch / headless automation.

---

## Architecture

```
LLM (Claude)  -->  MCP Protocol  -->  FastMCP Server (server.py)
                                           |
                                           v
                                  C# Script Generator
                                 (QuietModeStep wrapper)
                                           |
                                           v
                                 EPLAN Process (P8)
```

How execution works internally (`eplan_connection.py::execute_action(action, quiet_mode=True)`):

1. Parse the action name and parameters.
2. Generate a `.cs` script that runs the action inside
   `using (var qm = new QuietModeStep(QuietModes.ShowNoDialogs)) { ... }`.
3. `RegisterScript` → `ExecuteScript` → read a JSON result file → `UnregisterScript`.
4. Return `{"success": bool, "parameters": {...}}`, where `parameters` are the
   values EPLAN wrote back into the `ActionCallingContext` (e.g. `PROJECT`, `PAGES`).

The script-management utilities themselves (`RegisterScript`, `ExecuteScript`,
`UnregisterScript`) always run directly to avoid infinite recursion.

---

## Directory Structure

```
eplan-p8-mcp-server/
├── mcp_server/
│   ├── api/
│   │   └── actions/              # QuietMode python action wrappers
│   │       ├── _base.py          # QuietManagerWrapper, _build_action
│   │       ├── scripted.py       # advanced APIs via C# (parts DB, typed settings, PathMap)
│   │       ├── __init__.py       # re-exports every action and defines __all__
│   │       └── *.py              # one module per action category
│   ├── scripts/
│   │   ├── generated/            # temporary C# scripts (auto-created, auto-deleted)
│   │   └── results/              # temporary JSON results (auto-created, auto-deleted)
│   ├── server.py                 # MCP server: connection tools + dynamic action registration
│   ├── eplan_connection.py       # connection manager + QuietMode wrapper + version auto-detection
│   ├── requirements.txt
│   └── README.md                 # This file
└── tools/
    ├── validate_actions.py       # cross-check wrappers against the official docs RAG
    └── action_validation_report.md
```

> Note: both `eplan_connection.py` and `api/actions/scripted.py` write their
> temporary scripts/results under the single `scripts/generated` and
> `scripts/results` folders.

---

## Requirements

- **EPLAN Electric P8** installed (2024, 2025, 2026, or 2027)
- **Python 3.10+** (64-bit, to match EPLAN's process)
- Dependencies: `pip install -r requirements.txt` (`pythonnet`, `mcp`)

---

## Installation for Claude Code

### 1. Install dependencies

```bash
cd eplan-p8-mcp-server\mcp_server
pip install -r requirements.txt
```

### 2. Register the MCP server

```bash
claude mcp add eplan -- python YOUR_PATH\eplan-p8-mcp-server\mcp_server\server.py
claude mcp list   # "eplan" should appear
```

Or add it manually to `%USERPROFILE%\.claude\settings.json`:

```json
{
  "mcpServers": {
    "eplan": {
      "command": "python",
      "args": ["YOUR_PATH\\eplan-p8-mcp-server\\mcp_server\\server.py"]
    }
  }
}
```

### 3. Connect

Start EPLAN, open Claude Code, and say `connect to eplan`.

---

## Tools

### 1. Connection & utility tools

| Tool | Description |
|------|-------------|
| `eplan_versions` | List installed EPLAN versions (from disk, loads no DLLs). |
| `eplan_servers` | Detect active EPLAN instances on the machine. |
| `eplan_connect` | Connect to EPLAN. Optional `host` (remote machines, `"host:port"` accepted), `port` (auto-detected on localhost) and `version` (auto = newest installed). |
| `eplan_status` | Current connection details, including the targeted version. |
| `eplan_ping` | Check the connected instance is responding. |
| `eplan_test` | Show a MessageBox inside EPLAN to verify end-to-end communication. |
| `eplan_disconnect` | Close the active connection. |

### 2. Action tools (149)

Every EPLAN action is exposed as `eplan_<action>`. Each tool's description and
input schema are generated from the underlying Python function's docstring and
type hints, so the connected LLM discovers what is available and how to call it
automatically.

Action categories:

| Category | Examples |
|----------|----------|
| Project | `open_project`, `close_project`, `get_current_project`, `compress_project`, `synchronize_project` |
| Backup / restore | `backup_project`, `backup_masterdata`, `restore_project`, `restore_masterdata` |
| Export | `export_pdf_project`, `export_pdf_pages`, `export_dxf_*`, `export_dwg_*`, `export_graphics_*`, `export_pxf_project`, `export_3d` |
| Import | `import_pxf_project`, `import_dwg_page`, `import_dxf_page`, `import_dxfdwg_files`, `import_pdf_comments`, `import_3d` |
| Print | `print_project`, `print_pages` |
| Check / verify | `check_project`, `check_pages`, `check_parts` |
| Generate | `generate_connections`, `generate_cables` |
| Reports | `update_reports`, `update_model_view_pages`, `create_model_views`, `create_copper_unfolds`, `create_drilling_views` |
| Search | `search_devices`, `search_text`, `search_all_properties`, `search_page_data`, `search_project_data` |
| Navigation / edit | `edit_open_page`, `edit_goto_device`, `edit_open_layout_space`, `close_pages`, `get_selected_pages`, `preview_page`, `navigate_to_eec` |
| Renumber | `renumber_devices`, `renumber_pages`, `renumber_cables`, `renumber_terminals`, `renumber_connections` |
| Translate | `translate_project`, `export_missing_translations`, `remove_language` |
| Device list | `export_device_list`, `import_device_list`, `delete_device_list` |
| Labels / layers | `create_labels`, `change_layer`, `export/import_graphical_layer_table` |
| Macros | `generate_macros`, `prepare_macros`, `update_macros` |
| Scripts | `register_script`, `unregister_script`, `execute_script` |
| Settings | `export_settings`, `import_settings`, `set_setting`, `set_project_setting` |
| Properties | `get/set_project_property`, `get/set_page_property`, `get/set_property`, `export/import_user_properties` |
| Parts | `export/import_parts_list`, `select_part`, `set_parts_data_source`, `partsmanagement_*` |
| PLC | `plc_export`, `plc_import` |
| Workspace | `open_workspace`, `save_workspace`, `clean_workspace` |
| Data exchange | `export_connections/functions/pages`, `dc_import`, `dc_export`, `export_*_definitions`, `export/import_subproject`, `masterdata_operation`, … |
| Cabinet / 3D | `calculate_cabinet_weight`, `update_segments_filling`, `topology_operation`, `import_preplanning_data`, `export/import_segments_template` |
| Production | `export_nc_data`, `export_production_wiring` |
| Ribbon / add-ons | `export/import_ribbon_bar`, `load_api_module`, `register/unregister_addon`, `execute_raw_action` |
| Scripted (advanced APIs via C#) | `parts_db_query/count/get_part/update/list_product_groups`, `settings_get/set_string/bool/int/double`, `pathmap_substitute`, `pathmap_get_common_paths`, `execute_custom_script` |

---

## Extending: add a new action

The server registers tools **dynamically** from the actions package's `__all__`
list — there is no per-tool `@mcp.tool()` boilerplate to write.

1. Implement the function in `api/actions/<module>.py`:

   ```python
   def my_action(project_name: str = None) -> dict:
       """One-line summary the LLM will see as the tool description.

       Args:
           project_name: Project path (optional).
       """
       manager, error = _get_connected_manager()
       if error:
           return error
       action = _build_action("SomeEplanAction", PROJECTNAME=project_name)
       return manager.execute_action(action)
   ```

2. Export it in `api/actions/__init__.py`: add it to the imports **and** to
   `__all__`.

3. Restart the MCP server. The tool appears as `eplan_my_action`.

Tips:
- Write a meaningful docstring + type hints — they become the tool description
  and input schema the LLM relies on.
- Verify action names/parameters against the official EPLAN P8 docs (see the
  remote RAG at `https://rag2026.covaga.xyz`), then run
  `python ../tools/validate_actions.py` to cross-check the whole wrapper set.
- Windows paths need escaping (`\\`) or forward slashes (`/`).

---

## EPLAN version selection (automatic)

Nothing to configure. `eplan_connection.py::detect_installed_versions()` scans
`C:\Program Files\EPLAN\Platform` (override with the `EPLAN_PLATFORM_ROOT`
environment variable) and:

- **Auto (default):** targets the newest installed version and selects the
  matching .NET runtime (coreclr for EPLAN 2027+, .NET Framework for ≤ 2026).
- **Explicit:** `eplan_connect(version="2026")` targets a specific major
  version; `eplan_versions` lists the options without loading any DLLs.

Once one version's DLLs are loaded into the process, switching versions
requires restarting the MCP server (the .NET runtime cannot be swapped at
runtime).

---

## Example session

```
User: Connect to EPLAN and open "C:\Projects\Test.elk".
LLM:  [eplan_connect]         -> Connected on port 49152
      [eplan_open_project]    -> {"success": true, "parameters": {"PROJECT": "C:\\Projects\\Test.elk"}}
      Project opened silently (QuietMode).
```

See [`../../llm.md`](../../llm.md) for an operating guide aimed at the connected LLM.
