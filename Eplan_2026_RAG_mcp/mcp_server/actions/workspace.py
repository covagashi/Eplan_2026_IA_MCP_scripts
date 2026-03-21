"""
Workspace actions.
"""

from ._base import _get_connected_manager, _build_action


def open_workspace(workspace_path: str) -> dict:
    """
    Open an existing workspace.
    Action: OpenWorkspaceAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "OpenWorkspaceAction",
        WORKSPACEPATH=workspace_path
    )
    return manager.execute_action(action)


def save_workspace(workspace_path: str) -> dict:
    """
    Save the current workspace.
    Action: SaveWorkspaceAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "SaveWorkspaceAction",
        WORKSPACEPATH=workspace_path
    )
    return manager.execute_action(action)


def clean_workspace() -> dict:
    """
    Clean the current workspace.
    Action: CleanWorkspaceAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("CleanWorkspaceAction")
