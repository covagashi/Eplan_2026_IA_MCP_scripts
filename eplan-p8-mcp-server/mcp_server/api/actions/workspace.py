"""
Workspace actions.

Note: these actions need a mainframe (GUI). Under a headless/remote QuietMode
session they may not behave as in interactive mode.
"""

from ._base import _get_connected_manager, _build_action


def open_workspace(workspace_name: str, silent: bool = False) -> dict:
    """
    Open an existing workspace.
    Action: OpenWorkspaceAction

    Args:
        workspace_name: Name of the workspace to open (parameter Workspacename).
                        Use "?" to list all available workspaces.
        silent: Run in silent mode, suppressing dialogs (parameter Silent).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "OpenWorkspaceAction",
        Workspacename=workspace_name,
        Silent=silent
    )
    return manager.execute_action(action)


def save_workspace(workspace_name: str, silent: bool = False) -> dict:
    """
    Save the specified workspace. Created if it does not yet exist.
    Action: SaveWorkspaceAction

    Args:
        workspace_name: Name of the workspace to save (parameter Workspacename).
        silent: Run in silent mode, suppressing dialogs (parameter Silent).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "SaveWorkspaceAction",
        Workspacename=workspace_name,
        Silent=silent
    )
    return manager.execute_action(action)


def clean_workspace(workspace_name: str = None, silent: bool = False) -> dict:
    """
    Clean an existing workspace.
    Action: CleanWorkspaceAction

    Args:
        workspace_name: Name of the workspace to clean (parameter Workspacename).
                        If empty, the LAST_USED workspace is cleaned.
        silent: Run in silent mode, suppressing dialogs (parameter Silent).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "CleanWorkspaceAction",
        Workspacename=workspace_name,
        Silent=silent
    )
    return manager.execute_action(action)
