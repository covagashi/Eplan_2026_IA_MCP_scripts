# EPLAN MCP Server

Remote control of EPLAN from Claude via MCP (Model Context Protocol).

## Requirements

- EPLAN installed (2024, 2025, or 2026)
- Python 3.10+
- Dependencies: `pip install pythonnet mcp`

## Installation for Claude CLI (Claude Code)

### 1. Install Dependencies

```bash
cd YOUR_PATH\LazyScriptingEplan\mcp_server
pip install pythonnet mcp
```

### 2. Configure Claude CLI

Edit your Claude CLI settings file. The location depends on your system:

**Windows:**
```
%USERPROFILE%\.claude\settings.json
```

**Linux/macOS:**
```
~/.claude/settings.json
```

Add the MCP server configuration:

```json
{
  "mcpServers": {
    "eplan": {
      "command": "python",
      "args": ["YOUR_PATH\\LazyScriptingEplan\\mcp_server\\server.py"]
    }
  }
}
```

> **Note:** On Linux/macOS, use forward slashes: `"/path/to/mcp_server/server.py"`

### 3. Restart Claude CLI

Close and reopen Claude CLI for the changes to take effect.

## Installation for Claude Desktop

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "eplan": {
      "command": "python",
      "args": ["YOUR_PATH\\LazyScriptingEplan\\mcp_server\\server.py"]
    }
  }
}
```

Restart Claude Desktop.

## Usage

1. Open EPLAN manually
2. In Claude, use the available tools:
   - `eplan_servers` - Detect active EPLAN instances
   - `eplan_connect` - Connect to EPLAN (port auto-detected)
   - `eplan_status` - Get connection status
   - `eplan_ping` - Verify EPLAN is responding
   - `eplan_test` - Show a MessageBox in EPLAN (connection test)
   - `eplan_close_project` - Close the current project
   - `eplan_disconnect` - Disconnect from EPLAN

## Example Session

```
User: Connect to EPLAN
Claude: [calls eplan_connect]
       Connected to EPLAN at localhost:49152

User: Test the connection
Claude: [calls eplan_test]
       Check EPLAN for MessageBox

User: Close the project
Claude: [calls eplan_close_project]
       Executed: XPrjActionProjectClose
```

## Troubleshooting

### "EPLAN not found in Program Files"
Ensure EPLAN is installed in the default location. If installed elsewhere, update the paths in `eplan_connection.py`.

### "pythonnet not installed"
Run: `pip install pythonnet`

### "Not connected"
Make sure EPLAN is running before calling `eplan_connect`.

### Connection timeout
EPLAN must be fully loaded (not just starting up). Wait until the EPLAN interface is responsive.
