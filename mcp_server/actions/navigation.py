"""
Edit and navigation actions.
"""

from ._base import _get_connected_manager, _build_action


def edit_open_page(
    page_name: str,
    project_name: str = None,
    x: float = None,
    y: float = None
) -> dict:
    """
    Open a specific page in the editor.
    Action: edit

    Args:
        page_name: Page name to open
        project_name: Project path (optional)
        x: X coordinate to position cursor
        y: Y coordinate to position cursor
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "edit",
        PROJECTNAME=project_name,
        PAGENAME=page_name,
        X=x,
        Y=y
    )
    return manager.execute_action(action)


def edit_goto_device(
    device_name: str,
    project_name: str = None
) -> dict:
    """
    Navigate to a device in the project.
    Action: edit
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "edit",
        PROJECTNAME=project_name,
        DEVICENAME=device_name
    )
    return manager.execute_action(action)


def edit_open_layout_space(
    installation_space: str,
    project_name: str = None
) -> dict:
    """
    Open a layout/installation space.
    Action: edit
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "edit",
        PROJECTNAME=project_name,
        INSTALLATIONSPACE=installation_space
    )
    return manager.execute_action(action)


def close_pages() -> dict:
    """
    Close all selected pages in the editor.
    Action: XGedClosePage
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("XGedClosePage")


def redraw_ged() -> dict:
    """
    Redraw the graphical editor.
    Action: gedRedraw
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("gedRedraw")


def get_selected_pages() -> dict:
    """
    Get selected pages.
    Action: selectionset
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "selectionset",
        TYPE="SELECTEDPAGES"
    )
    return manager.execute_action(action)


def preview_page(page_name: str = None, project_name: str = None, open: bool = True) -> dict:
    """
    Open or close page preview.
    Action: XSDPreviewAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSDPreviewAction",
        PROJECTNAME=project_name,
        PAGENAME=page_name,
        OPEN="1" if open else "0"
    )
    return manager.execute_action(action)


def navigate_to_eec(object_id: str) -> dict:
    """
    Navigate to object in EPLAN Engineering Configuration.
    Action: navigateToEEC
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "navigateToEEC",
        OBJECTID=object_id
    )
    return manager.execute_action(action)
