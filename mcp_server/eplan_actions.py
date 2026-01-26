"""
EPLAN Actions
Verified EPLAN actions that work correctly.

To add a new action:
1. Verify it works in EPLAN
2. Add the function here
3. Register it in server.py with @mcp.tool()
"""

import json
from eplan_connection import get_manager

TARGET_VERSION = "2026"


def close_project() -> dict:
    """
    Close the currently open project in EPLAN.
    Action: XPrjActionProjectClose
    """
    manager = get_manager(TARGET_VERSION)

    if not manager.connected:
        return {
            "success": False,
            "message": "Not connected to EPLAN"
        }

    return manager.execute_action("XPrjActionProjectClose")


# ============================================================================
# TEMPLATE FOR NEW ACTIONS
# ============================================================================
#
# def new_action(parameter: str) -> dict:
#     """
#     Description of what it does.
#     Action: EPLANActionName
#     """
#     manager = get_manager(TARGET_VERSION)
#
#     if not manager.connected:
#         return {"success": False, "message": "Not connected to EPLAN"}
#
#     return manager.execute_action(f'EPLANActionName /Param:"{parameter}"')
#
# ============================================================================
