"""
EPLAN MCP Server

Complete EPLAN automation server exposing all API actions via MCP protocol.
Organized in V1 (legacy direct execution) and V2 (C# scripted execution with QuietMode).

Requirements:
- EPLAN installed
- pip install pythonnet mcp
"""

import json
import os
import sys
import functools
from mcp.server.fastmcp import FastMCP
from eplan_connection import get_manager

TARGET_VERSION = "2025"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

mcp = FastMCP("EPLAN MCP Server")

# Add API folders to path for imports
sys.path.insert(0, os.path.join(SCRIPT_DIR, "api"))

# Import versioned action modules
import api.v1.actions as actions_v1
import api.v2.actions as actions_v2


# ============================================================================
# CONNECTION MANAGEMENT (Shared / Version-Agnostic)
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
    """Connect to EPLAN. Port is auto-detected if not specified."""
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
# DYNAMIC VERSIONED ACTIONS REGISTRATION (V1 and V2)
# ============================================================================

def register_actions(actions_module, version_prefix, description_prefix):
    """
    Dynamically registers all actions exported by the actions module.
    Wraps the functions to return formatted JSON.
    """
    for func_name in actions_module.__all__:
        if func_name.startswith('_') or func_name == 'TARGET_VERSION':
            continue
            
        func = getattr(actions_module, func_name)
        if not callable(func):
            continue
            
        tool_name = f"eplan_{version_prefix}_{func_name}"
        
        def make_wrapper(f):
            @functools.wraps(f)
            def mcp_tool_wrapper(*args, **kwargs):
                try:
                    res = f(*args, **kwargs)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                except Exception as e:
                    return json.dumps({"success": False, "error": str(e)}, indent=2)
            
            # Format docstring to include version prefix info
            doc = f.__doc__ or ""
            # Strip common indentation
            lines = doc.split('\n')
            if len(lines) > 1:
                first_line = lines[0]
                rest = "\n".join(lines[1:])
                doc = f"{first_line}\n\n[{description_prefix}]\n{rest}"
            else:
                doc = f"{doc}\n\n[{description_prefix}]"
                
            mcp_tool_wrapper.__doc__ = doc
            return mcp_tool_wrapper
            
        wrapped_tool = make_wrapper(func)
        mcp.tool(name=tool_name)(wrapped_tool)


# Register V1 legacy direct actions
register_actions(actions_v1, "v1", "V1 - Runs EPLAN actions directly via Remote API.")

# Register V2 QuietMode script actions
register_actions(actions_v2, "v2", "V2 - Runs EPLAN actions inside a C# script wrapping under QuietMode to suppress dialogs.")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("EPLAN MCP Server")
    print(f"Target: EPLAN {TARGET_VERSION}")
    print("-" * 40)
    print("Running in dual version mode:")
    print("  - V1 prefix: eplan_v1_* (Direct Remote API)")
    print("  - V2 prefix: eplan_v2_* (C# Script in QuietMode)")
    print("-" * 40)
    mcp.run()
