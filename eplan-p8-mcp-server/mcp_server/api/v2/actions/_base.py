"""
Base utilities for EPLAN actions.
Shared functions used by all action modules.
"""

from typing import Optional
import sys
import os

# Add parent directory to path for imports
mcp_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if mcp_root not in sys.path:
    sys.path.insert(0, mcp_root)

# Also insert the current folder's parent so 'from .project import ...' style works if needed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from eplan_connection import get_manager

TARGET_VERSION = "2027"


class V2ManagerWrapper:
    """Wrapper that forces execute_action to run with quiet_mode=True (via script)."""
    def __init__(self, manager):
        self.manager = manager

    def __getattr__(self, name):
        if name == "execute_action":
            # Direct everything to execute_action with quiet_mode=True
            return lambda action, *args, **kwargs: self.manager.execute_action(action, quiet_mode=True)
        return getattr(self.manager, name)


def _get_connected_manager():
    """Get the connection manager, ensuring it's connected."""
    manager = get_manager(TARGET_VERSION)
    if not manager.connected:
        return None, {"success": False, "message": "Not connected to EPLAN. Call eplan_connect() first."}
    return V2ManagerWrapper(manager), None


def _build_action(action_name: str, **params) -> str:
    """Build an action string with parameters."""
    parts = [action_name]
    for key, value in params.items():
        if value is not None and value != "":
            if isinstance(value, bool):
                value = "1" if value else "0"
            # Quote strings with spaces
            if isinstance(value, str) and " " in value and not value.startswith('"'):
                value = f'"{value}"'
            parts.append(f"/{key}:{value}")
    return " ".join(parts)


def _execute_with_quiet_mode(action: str) -> dict:
    """Execute an action with QuietMode enabled to suppress dialogs."""
    manager, error = _get_connected_manager()
    if error:
        return error
    return manager.execute_action(action, quiet_mode=True)
