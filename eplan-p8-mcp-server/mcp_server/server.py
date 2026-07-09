"""
EPLAN MCP Server

Complete EPLAN automation server exposing all API actions via MCP protocol.
Every action runs inside a C# script under QuietMode (no blocking dialogs).

Requirements:
- EPLAN installed
- pip install pythonnet mcp
"""

import json
import os
import sys
import functools
from mcp.server.fastmcp import FastMCP
from eplan_connection import get_manager, detect_installed_versions

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

mcp = FastMCP("EPLAN MCP Server")

# Add API folders to path for imports
sys.path.insert(0, os.path.join(SCRIPT_DIR, "api"))

# Import the actions package (QuietMode execution)
import api.actions as eplan_actions


# ============================================================================
# CONNECTION MANAGEMENT (Shared / Version-Agnostic)
# ============================================================================

@mcp.tool()
def eplan_status() -> str:
    """Get the current EPLAN connection status."""
    manager = get_manager()
    return json.dumps(manager.get_status(), indent=2)


@mcp.tool()
def eplan_versions() -> str:
    """List EPLAN versions installed on this machine.

    Use this BEFORE eplan_connect if the user needs a specific version;
    by default the newest installed version is used automatically.
    Does not load any EPLAN DLLs, so it never locks the process to a version.
    """
    installed = detect_installed_versions()
    manager = get_manager()
    return json.dumps({
        "installed": installed,
        "loaded_version": manager.target_version if manager._clr_initialized else None,
        "note": "Pass version to eplan_connect to target one explicitly; omit it to auto-use the newest.",
    }, indent=2)


@mcp.tool()
def eplan_servers() -> str:
    """List active EPLAN servers (running instances).

    Note: this loads the EPLAN DLLs (auto-detected newest version if not
    connected yet).
    """
    manager = get_manager()
    servers = manager.get_active_servers()
    return json.dumps({"servers": servers, "count": len(servers)}, indent=2)


@mcp.tool()
def eplan_connect(host: str = None, port: str = None, version: str = None) -> str:
    """Connect to EPLAN.

    Args:
        host: EPLAN machine to connect to. Defaults to "localhost". Set this to
            reach an EPLAN instance on another machine (e.g. "10.10.10.2"). You
            may also pass "host:port" as this argument and it will be split.
        port: Remoting port. Auto-detected from local servers if omitted, but
            auto-detection only works for localhost — when connecting to a
            remote host you must supply the port explicitly (default 49152).
        version: EPLAN major version to target, e.g. "2026". Omit for
            auto-detection (newest installed version). Use eplan_versions to
            see what is available. Once one version's DLLs are loaded,
            switching requires restarting the MCP server.
    """
    # Allow "10.10.10.2:49152" passed as either host or port.
    if host and ":" in host and port is None:
        host, port = host.rsplit(":", 1)
    elif port and ":" in port:
        maybe_host, maybe_port = port.rsplit(":", 1)
        if maybe_port.isdigit():
            host, port = maybe_host, maybe_port

    manager = get_manager(version)
    result = manager.connect(host=host, port=port)
    result["target_version"] = manager.target_version
    return json.dumps(result, indent=2)


@mcp.tool()
def eplan_disconnect() -> str:
    """Disconnect from EPLAN."""
    manager = get_manager()
    return json.dumps(manager.disconnect(), indent=2)


@mcp.tool()
def eplan_ping() -> str:
    """Check if EPLAN is responding."""
    manager = get_manager()
    return json.dumps(manager.ping(), indent=2)


@mcp.tool()
def eplan_test() -> str:
    """
    Show a MessageBox in EPLAN to verify the connection is working.
    Creates and executes a temporary C# script.
    """
    manager = get_manager()

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
# DYNAMIC ACTIONS REGISTRATION
# ============================================================================

def register_actions(actions_module):
    """
    Dynamically registers all actions exported by the actions module.
    Wraps the functions to return formatted JSON.
    """
    for func_name in actions_module.__all__:
        if func_name.startswith('_'):
            continue

        func = getattr(actions_module, func_name)
        if not callable(func):
            continue

        tool_name = f"eplan_{func_name}"

        def make_wrapper(f):
            @functools.wraps(f)
            def mcp_tool_wrapper(*args, **kwargs):
                try:
                    res = f(*args, **kwargs)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                except Exception as e:
                    return json.dumps({"success": False, "error": str(e)}, indent=2)

            mcp_tool_wrapper.__doc__ = f.__doc__ or ""
            return mcp_tool_wrapper

        wrapped_tool = make_wrapper(func)
        mcp.tool(name=tool_name)(wrapped_tool)


# Register all actions (executed inside a C# script under QuietMode)
register_actions(eplan_actions)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    installed = detect_installed_versions()
    print("EPLAN MCP Server")
    if installed:
        versions = ", ".join(i["full_version"] for i in installed)
        print(f"Installed EPLAN versions: {versions} (auto-targets the newest)")
    else:
        print("WARNING: no EPLAN installation detected")
    print("-" * 40)
    print("All actions run as eplan_* (C# script under QuietMode)")
    print("-" * 40)
    mcp.run()
