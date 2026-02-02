"""
Ribbon bar customization actions.
"""

from ._base import _get_connected_manager, _build_action


def export_ribbon_bar(export_file: str) -> dict:
    """
    Export main ribbon bar customization to XML.
    Action: MfExportRibbonBarAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "MfExportRibbonBarAction",
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def import_ribbon_bar(import_file: str) -> dict:
    """
    Import main ribbon bar customization from XML.
    Action: MfImportRibbonBarAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "MfImportRibbonBarAction",
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)
