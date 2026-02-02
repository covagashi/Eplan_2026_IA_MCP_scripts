"""
Layer management actions.
"""

from ._base import _get_connected_manager, _build_action


def change_layer(
    layer_name: str = None,
    visible: bool = None,
    printable: bool = None,
    editable: bool = None
) -> dict:
    """
    Change graphical layer properties.
    Action: changelayer
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "changelayer",
        LAYERNAME=layer_name,
        VISIBLE=visible,
        PRINTABLE=printable,
        EDITABLE=editable
    )
    return manager.execute_action(action)


def export_graphical_layer_table(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export graphical layer table.
    Action: graphicallayertable
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "graphicallayertable",
        TYPE="EXPORT",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def import_graphical_layer_table(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import graphical layer table.
    Action: graphicallayertable
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "graphicallayertable",
        TYPE="IMPORT",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)
