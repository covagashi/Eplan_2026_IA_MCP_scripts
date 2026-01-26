"""
EPLAN MCP Server

Requirements:
- EPLAN installed
- pip install pythonnet mcp
"""

import json
import os
from mcp.server.fastmcp import FastMCP
from eplan_connection import get_manager
from eplan_actions import close_project

TARGET_VERSION = "2026"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

mcp = FastMCP("EPLAN MCP Server")


# ============================================================================
# CONNECTION
# ============================================================================

@mcp.tool()
def eplan_status() -> str:
    """Get the current EPLAN connection status."""
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.get_status(), indent=2)


@mcp.tool()
def eplan_servers() -> str:
    """List active EPLAN servers (running instances)."""
    manager = get_manager(TARGET_VERSION)
    servers = manager.get_active_servers()
    return json.dumps({"servers": servers, "count": len(servers)}, indent=2)


@mcp.tool()
def eplan_connect(port: str = None) -> str:
    """
    Connect to EPLAN. Port is auto-detected if not specified.
    """
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.connect(port=port), indent=2)


@mcp.tool()
def eplan_disconnect() -> str:
    """Disconnect from EPLAN."""
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.disconnect(), indent=2)


@mcp.tool()
def eplan_ping() -> str:
    """Check if EPLAN is responding."""
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.ping(), indent=2)


# ============================================================================
# EPLAN ACTIONS (verified)
# ============================================================================

@mcp.tool()
def eplan_close_project() -> str:
    """Close the currently open project. Action: XPrjActionProjectClose"""
    return json.dumps(close_project(), indent=2)


# ============================================================================
# TEST - MessageBox in EPLAN
# ============================================================================

@mcp.tool()
def eplan_test() -> str:
    """
    Show a MessageBox in EPLAN to verify the connection is working.
    Creates and executes a temporary C# script.
    """
    manager = get_manager(TARGET_VERSION)

    if not manager.connected:
        return json.dumps({
            "success": False,
            "message": "Not connected. Call eplan_connect() first."
        }, indent=2)

    # Create test script
    scripts_dir = os.path.join(SCRIPT_DIR, "scripts")
    os.makedirs(scripts_dir, exist_ok=True)
    script_path = os.path.join(scripts_dir, "mcp_test.cs")

    script = '''using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class MCPTest
{
    [Start]
    public void Run()
    {
        MessageBox.Show(
            "MCP Connection OK!",
            "EPLAN MCP Server",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information
        );
    }
}
'''
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script)

    # Register and execute
    manager.execute_action(f'RegisterScript /ScriptFile:"{script_path}"')
    result = manager.execute_action(f'ExecuteScript /ScriptFile:"{script_path}"')

    return json.dumps({
        "success": result.get("success", False),
        "message": "Check EPLAN for MessageBox" if result.get("success") else result.get("message")
    }, indent=2)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("EPLAN MCP Server")
    print(f"Target: EPLAN {TARGET_VERSION}")
    print("-" * 40)
    mcp.run()
