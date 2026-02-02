"""
Base utilities for EPLAN actions.
Shared functions used by all action modules.
"""

from typing import Optional
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eplan_connection import get_manager

TARGET_VERSION = "2026"


def _get_connected_manager():
    """Get the connection manager, ensuring it's connected."""
    manager = get_manager(TARGET_VERSION)
    if not manager.connected:
        return None, {"success": False, "message": "Not connected to EPLAN. Call eplan_connect() first."}
    return manager, None


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
