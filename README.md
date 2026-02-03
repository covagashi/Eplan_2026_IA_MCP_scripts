# EPLAN Automation Tools

This repository contains tools for automating EPLAN Electric P8 using AI assistants.
Currently is 100% functional

## MCP Server (Recommended)

The **MCP Server** (`mcp_server/`) allows any AI to control EPLAN directly through the Model Context Protocol.

### What is MCP?

**MCP (Model Context Protocol)** is an open standard that allows AI assistants like Claude to interact with external tools and services. Instead of just generating code, Claude can actually *execute* actions in EPLAN in real-time.

With MCP, you can:
- Connect to a running EPLAN instance
- Execute EPLAN actions directly from Claude
- Get real-time feedback on operations
- Automate complex workflows through natural conversation

### Prerequisites

- **Python 3.10+** installed and added to PATH
- **EPLAN Electric P8** installed (2024 or later recommended)
- **Claude Code CLI** installed ([Installation guide](https://docs.anthropic.com/claude-code))

### Installation Steps

#### Step 1: Install Python Dependencies

Open a terminal and run:

```bash
pip install pythonnet mcp
```

#### Step 2: Configure Claude Code CLI

Add the MCP server to Claude Code. Replace `YOURPATH` with the actual path to the scripts folder:

```bash
claude mcp add eplan -- python YOURPATH\Eplan_2026_IA_MCP_scripts\mcp_server\server.py
```

**Example with full path:**
```bash
claude mcp add eplan -- python D:\1_GENERAL\Eplan_2026_IA_MCP_scripts\mcp_server\server.py
```

#### Step 3: Verify Configuration

Check that the MCP server was added correctly:

```bash
claude mcp list
```

You should see `eplan` in the list of configured MCP servers.

#### Step 4: Start EPLAN

1. Open EPLAN Electric P8
2. Make sure it's fully loaded before connecting

#### Step 5: Start Claude Code and Connect

1. Open a terminal and run `claude`
2. Ask Claude to connect to EPLAN:
   ```
   connect to eplan
   ```
3. Claude will auto-detect the running EPLAN instance and connect

### Troubleshooting

| Issue | Solution |
|-------|----------|
| "pythonnet not found" | Run `pip install pythonnet` |
| "Cannot connect to EPLAN" | Make sure EPLAN is running and fully loaded |
| "MCP server not found" | Check the path in `claude mcp list` and verify the file exists |
| "Port not found" | EPLAN API server may not be running; restart EPLAN |

### Uninstalling

To remove the MCP server from Claude Code:

```bash
claude mcp remove eplan
```

![Claude cli configured](image.png)

---

## Adding New EPLAN Actions

The MCP server is designed to be easily extensible. Here's how to add new EPLAN actions:


### Step 1: Add the Function to `eplan_actions.py`

```python
def example_project(project_path: str) -> dict:
    """
    Open an EPLAN project.
    Action: example
    """
    manager = get_manager(TARGET_VERSION)

    if not manager.connected:
        return {"success": False, "message": "Not connected to EPLAN"}

    # Note: Use forward slashes or escape backslashes in the path
    return manager.execute_action(f'example /param1:"{project_path}"')
```

### Step 3: Register the Tool in `server.py`

```python
from eplan_actions import close_project, example_project  # Add your import

@mcp.tool()
def example_project(project_path: str) -> str:
    """Open an EPLAN project by path."""
    return json.dumps(example_project(project_path), indent=2)
```

### Step 4: Restart Claude CLI

The new tool will be available after restarting Claude CLI.

![Eplan test](image-1.png)

### Tips for Adding Actions

1. **Test in EPLAN first** - Use EPLAN's scripting to verify the action works
2. **Check parameters** - Each action has specific parameters; refer to the API documentation
3. **Handle paths carefully** - Windows paths need escaping or use forward slashes
4. **Add meaningful docstrings** - Claude uses the docstring to understand when to use the tool

---

## OG Project Structure

```
LazyScriptingEplan/
├── mcp_server/                 # MCP Server for Claude integration
│   ├── server.py               # Main MCP server with tool definitions
│   ├── eplan_connection.py     # EPLAN connection management
│   ├── eplan_actions.py        # EPLAN action implementations
│   └── README.md               # MCP installation guide
│
└── README.md                   # This file
```

---

## Resources

- [EPLAN API Documentation](https://www.eplan.help/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
