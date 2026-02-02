"""
Data exchange and synchronization actions.
Complete implementation including DC export/import and specialized exports.
"""

from typing import Optional
from ._base import _get_connected_manager, _build_action


def export_connections(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export connections from project.
    Action: XMExportConnectionsAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportConnectionsAction",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def export_functions(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export functions from project.
    Action: XMExportFunctionAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportFunctionAction",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def export_pages(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export pages from project.
    Action: XMExportPagesAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportPagesAction",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def dc_import(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import data configuration file into project.
    Action: XMActionDCImport
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMActionDCImport",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)


def dc_export(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export data configuration from project.
    Action: XMActionDCCommonExport
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMActionDCCommonExport",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def export_dc_article_data(
    destination: str,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False
) -> dict:
    """
    Export article data for external editing.
    Action: XMExportDCArticleDataAction

    Args:
        destination: Target file (TXT, XLSX, XML based on scheme)
        config_scheme: Configuration scheme (dialog shown if not set)
        language: Language code (e.g., "en_US")
        complete_project: Export whole database, not just selected objects
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return
        immediate_import: Auto-import after edit (only for mode 2)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportDCArticleDataAction",
        DESTINATION=destination,
        CONFIGSCHEME=config_scheme,
        LANGUAGE=language,
        COMPLETEPROJECT=complete_project,
        EXECUTIONMODE=execution_mode,
        IMMEDIATEIMPORT=immediate_import
    )
    return manager.execute_action(action)


def import_dc_article_data(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import article data from external editing.
    Action: XMImportDCArticleDataAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMImportDCArticleDataAction",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)


def export_location_boxes(
    destination: str,
    project_name: str = None,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False
) -> dict:
    """
    Export location boxes of a project.
    Note: Use dc_export (XMActionDCCommonExport) for new implementations.
    Action: XMExportLocationBoxesAction

    Args:
        destination: Target file (TXT, XLS, XML)
        project_name: Project path (optional)
        config_scheme: Configuration scheme
        language: Language code
        complete_project: Export all pages, not just selected
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return
        immediate_import: Auto-import after edit (only for mode 2)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportLocationBoxesAction",
        ProjectName=project_name,
        Destination=destination,
        ConfigScheme=config_scheme,
        Language=language,
        CompleteProject=complete_project,
        ExecutionMode=execution_mode,
        ImmediateImport=immediate_import
    )
    return manager.execute_action(action)


def export_potential_definitions(
    destination: str,
    project_name: str = None,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False
) -> dict:
    """
    Export potential definitions of a project.
    Note: Use dc_export (XMActionDCCommonExport) for new implementations.
    Action: XMExportPotentialDefsAction

    Args:
        destination: Target file (TXT, XLS, XML)
        project_name: Project path (optional)
        config_scheme: Configuration scheme
        language: Language code
        complete_project: Export all pages, not just selected
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return
        immediate_import: Auto-import after edit (only for mode 2)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportPotentialDefsAction",
        ProjectName=project_name,
        Destination=destination,
        ConfigScheme=config_scheme,
        Language=language,
        CompleteProject=complete_project,
        ExecutionMode=execution_mode,
        ImmediateImport=immediate_import
    )
    return manager.execute_action(action)


def export_pipeline_definitions(
    destination: str,
    project_name: str = None,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False
) -> dict:
    """
    Export pipeline definitions of a project.
    Action: XMExportPipeLineDefsAction

    Args:
        destination: Target file (TXT, XLS, XML)
        project_name: Project path (optional)
        config_scheme: Configuration scheme
        language: Language code
        complete_project: Export all pages, not just selected
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return
        immediate_import: Auto-import after edit (only for mode 2)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportPipeLineDefsAction",
        ProjectName=project_name,
        Destination=destination,
        ConfigScheme=config_scheme,
        Language=language,
        CompleteProject=complete_project,
        ExecutionMode=execution_mode,
        ImmediateImport=immediate_import
    )
    return manager.execute_action(action)


def delete_representation_type(
    project_name: str = None
) -> dict:
    """
    Delete representation type.
    Action: XMDeleteReprTypeAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMDeleteReprTypeAction",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def correct_connections() -> dict:
    """
    Merge graphical properties of connection definition points.
    Action: EsCorrectConnections
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("EsCorrectConnections")


def remove_unnecessary_ndps() -> dict:
    """
    Remove unnecessary net definition points.
    Action: XCMRemoveUnnecessaryNDPsAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("XCMRemoveUnnecessaryNDPsAction")


def unite_net_definition_points() -> dict:
    """
    Unite net definition points on the same net.
    Action: XCMUniteNetDefinitionPointsAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("XCMUniteNetDefinitionPointsAction")


def export_subproject(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export subproject.
    Action: subprojects
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "subprojects",
        TYPE="EXPORT",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def import_subproject(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import subproject.
    Action: subprojects
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "subprojects",
        TYPE="IMPORT",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)


def masterdata_operation(
    operation_type: str,
    source_path: str = None,
    destination_path: str = None
) -> dict:
    """
    Perform master data operations.
    Action: masterdata
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "masterdata",
        TYPE=operation_type,
        SOURCEPATH=source_path,
        DESTINATIONPATH=destination_path
    )
    return manager.execute_action(action)
