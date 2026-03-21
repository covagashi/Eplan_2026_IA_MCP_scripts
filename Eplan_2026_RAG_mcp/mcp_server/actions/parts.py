"""
Parts management actions.
"""

from ._base import _get_connected_manager, _build_action


def export_parts_list(
    export_file: str,
    project_name: str = None,
    format: str = None
) -> dict:
    """
    Export parts list from project.
    Action: partslist
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "partslist",
        TYPE="EXPORT",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file,
        FORMAT=format
    )
    return manager.execute_action(action)


def import_parts_list(
    import_file: str,
    project_name: str = None,
    format: str = None
) -> dict:
    """
    Import parts list into project.
    Action: partslist
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "partslist",
        TYPE="IMPORT",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file,
        FORMAT=format
    )
    return manager.execute_action(action)


def select_part() -> dict:
    """
    Start the part selection dialog.
    Action: XPamSelectPart
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("XPamSelectPart")


def set_parts_data_source(data_source: str) -> dict:
    """
    Change the parts management database type.
    Action: XPartsSetDataSourceAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XPartsSetDataSourceAction",
        DATASOURCE=data_source
    )
    return manager.execute_action(action)
