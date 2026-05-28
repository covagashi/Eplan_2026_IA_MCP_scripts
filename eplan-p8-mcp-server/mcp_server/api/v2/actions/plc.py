"""
PLC import/export actions.
"""

from ._base import _get_connected_manager, _build_action


def plc_export(
    export_file: str,
    project_name: str = None,
    converter: str = None
) -> dict:
    """
    Export PLC data.
    Action: plcservice
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "plcservice",
        TYPE="EXPORT",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file,
        CONVERTER=converter
    )
    return manager.execute_action(action)


def plc_import(
    import_file: str,
    project_name: str = None,
    converter: str = None
) -> dict:
    """
    Import PLC data.
    Action: plcservice
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "plcservice",
        TYPE="IMPORT",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file,
        CONVERTER=converter
    )
    return manager.execute_action(action)
