# EPLAN MCP Server (Dual API Mode)

Remote control of **EPLAN Electric P8** from Claude via MCP (Model Context Protocol).

The server runs in dual API mode:
- **V1 (Direct Execution)**: Calls EPLAN actions directly via the Remote Client API. Fast, but might prompt user confirmation dialogs if EPLAN requires them.
- **V2 (C# Scripted Execution - Recommended)**: Wraps EPLAN actions inside dynamically generated C# scripts executed inside EPLAN's process space under `QuietMode` (`QuietModes.ShowNoDialogs`). Completely silent, prevents blocking dialogs, and returns execution result parameters.

---

## Architecture

```
Claude Code  -->  MCP Protocol  -->  FastMCP Server (server.py)
                                           |
                              +------------+------------+
                              |                         |
                           [API V1]                  [API V2]
                       Direct Remoting API      C# Script Generator
                       (client.ExecuteAction)    (QuietModeStep)
                              |                         |
                              +------------+------------+
                                           |
                                           v
                                     EPLAN Process
```

---

## Directory Structure

The project has been reorganized for clear separation of versioned APIs:

```
eplan-p8-mcp-server/mcp_server/
├── api/
│   ├── v1/
│   │   ├── actions/          # Legacy python action wrappers (direct execution)
│   │   └── __init__.py
│   └── v2/
│       ├── actions/          # QuietMode python action wrappers (C# script wrapped)
│       └── __init__.py
├── scripts/
│   ├── generated/            # Directory where temporary V2 C# scripts are compiled
│   └── results/              # Directory where temporary V2 JSON results are stored
├── server.py                 # Main MCP server (exposes connection, RAG, V1 and V2 tools)
├── eplan_connection.py       # Shared EPLAN pythonnet connection manager
├── rag_engine.py             # Local Documentation RAG search engine (ChromaDB)
└── README.md                 # This file
```

---

## Requirements

- **EPLAN Electric P8** installed (2024, 2025, or 2026)
- **Python 3.10+** (64-bit to match EPLAN)
- Dependencies: `pip install -r requirements.txt`

---

## Installation for Claude CLI (Claude Code)

### 1. Install Dependencies

```bash
cd eplan-p8-mcp-server\mcp_server
pip install -r requirements.txt
```

### 2. Configure Claude CLI

Add the MCP server to your Claude CLI settings (`%USERPROFILE%\.claude\settings.json`):

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

---

## Usage

### 1. Shared Connection & Utility Tools
These tools manage the active EPLAN instance connection and are version-agnostic:
- `eplan_servers` - Detect active EPLAN instances running on the machine.
- `eplan_connect` - Establish connection to EPLAN (port auto-detected if omitted).
- `eplan_status` - Get current connection details.
- `eplan_ping` - Check if the connected EPLAN instance is responding.
- `eplan_test` - Show a MessageBox inside EPLAN to verify end-to-end communication.
- `eplan_disconnect` - Close the active connection.

### 2. Documentation RAG (Semantic Search)
Find EPLAN API classes, properties, actions, and documentation:
- `eplan_docs_search` - Perform a semantic search on local EPLAN guides/documentation.
- `eplan_docs_index` - Build/Re-build vector embeddings database (ChromaDB).
- `eplan_docs_stats` - View embedding stats.

### 3. Versioned Action Tools (149 tools per version)
Every EPLAN action (e.g. `open_project`, `export_pdf_project`, `create_labels`) is exposed in two forms:

*   **V1 Tools (`eplan_v1_<action_name>`)**
    Executes the action directly. Recommended only for simple tasks or when you want to see dialogs.
    
*   **V2 Tools (`eplan_v2_<action_name>`)**
    Executes the action wrapped inside a C# script running in EPLAN's AppDomain. This enables `QuietMode` (completely suppressing dialogs) and captures returned parameters.

---

## Example Session

```
User: Conéctate a EPLAN y abre el proyecto "C:\Projects\Test.elk" de manera silenciosa
Claude: [calls eplan_connect] -> Connected on port 49152
        [calls eplan_v2_open_project] -> {"success": true, "parameters": {"Project": "C:\\Projects\\Test.elk"}}
        Proyecto abierto en modo silencioso (V2).
```
