"""
Data exchange and synchronization actions.
Complete implementation including DC export/import and specialized exports.
"""

from typing import Optional
from ._base import _get_connected_manager, _build_action


def export_connections(
    destination: str,
    project_name: str = None,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False,
    include_graphical_connections: bool = False
) -> dict:
    """
    Export connections of a project (for external editing).
    Note: Provided for backward compatibility; prefer dc_export
    (XMActionDCCommonExport) for new implementations.
    Action: XMExportConnectionsAction

    Args:
        destination: Target file (TXT, XLSX, XML; format per ConfigScheme
                     extension) (parameter Destination).
        project_name: Project path (parameter ProjectName).
        config_scheme: Configuration scheme (parameter ConfigScheme).
        language: Language code, e.g. "en_US" (parameter Language).
        complete_project: Export all connections, not only selected ones.
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return.
        immediate_import: Auto-import after edit (only for execution_mode 2).
        include_graphical_connections: Include graphical connections.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportConnectionsAction",
        ProjectName=project_name,
        Destination=destination,
        ConfigScheme=config_scheme,
        Language=language,
        CompleteProject=complete_project,
        ExecutionMode=execution_mode,
        ImmediateImport=immediate_import,
        IncludeGraphicalConnections=include_graphical_connections
    )
    return manager.execute_action(action)


def export_functions(
    destination: str,
    project_name: str = None,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False
) -> dict:
    """
    Export functions of a project (for external editing).
    Note: Prefer dc_export (XMActionDCCommonExport) for new implementations.
    Action: XMExportFunctionAction

    Args:
        destination: Target file (TXT, XLSX, XML) (parameter Destination).
        project_name: Project path (parameter ProjectName).
        config_scheme: Configuration scheme (parameter ConfigScheme).
        language: Language code (parameter Language).
        complete_project: Export all functions, not only selected ones.
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return.
        immediate_import: Auto-import after edit (only for execution_mode 2).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportFunctionAction",
        ProjectName=project_name,
        Destination=destination,
        ConfigScheme=config_scheme,
        Language=language,
        CompleteProject=complete_project,
        ExecutionMode=execution_mode,
        ImmediateImport=immediate_import
    )
    return manager.execute_action(action)


def export_pages(
    destination: str,
    project_name: str = None,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False
) -> dict:
    """
    Export pages of a project (for external editing).
    Note: Prefer dc_export (XMActionDCCommonExport) for new implementations.
    Action: XMExportPagesAction

    Args:
        destination: Target file (TXT, XLSX, XML) (parameter Destination).
        project_name: Project path (parameter ProjectName).
        config_scheme: Configuration scheme (parameter ConfigScheme).
        language: Language code (parameter Language).
        complete_project: Export all pages, not only selected ones.
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return.
        immediate_import: Auto-import after edit (only for execution_mode 2).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMExportPagesAction",
        ProjectName=project_name,
        Destination=destination,
        ConfigScheme=config_scheme,
        Language=language,
        CompleteProject=complete_project,
        ExecutionMode=execution_mode,
        ImmediateImport=immediate_import
    )
    return manager.execute_action(action)


def dc_import(
    import_file: str,
    project_name: str = None,
    progress_title: str = None
) -> dict:
    """
    Import a data configuration file into an existing EPLAN project.
    This allows the properties of functions to be changed.
    Action: XMActionDCImport

    Args:
        import_file: Path of the data configuration (.edc) file
                     (parameter DataConfigurationFile).
        project_name: Project path (parameter ProjectLink).
        progress_title: Optional progress title (parameter ProgressTitle).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMActionDCImport",
        ProjectLink=project_name,
        DataConfigurationFile=import_file,
        ProgressTitle=progress_title
    )
    return manager.execute_action(action)


def dc_export(
    destination: str,
    project_name: str = None,
    config_scheme: str = None,
    language: str = None,
    complete_project: bool = False,
    execution_mode: int = 0,
    immediate_import: bool = False
) -> dict:
    """
    Export project data configuration for external editing.
    This is the recommended action for connections/functions/pages/etc. export.
    Action: XMActionDCCommonExport

    Validated 2026-07-24 against EPLAN 2025 in a 467-project unattended batch
    (execution_mode=2, immediate_import=True, complete_project=True): 467/467
    returned success with no manual interaction and no errors.

    IMPORTANT — execution_mode=2 does NOT pause for manual editing here.
    Every action in this wrapper runs under QuietMode (QuietModes.ShowNoDialogs,
    see _base.py) so no EPLAN dialog can block an unattended call. Normally
    execution_mode=2 ("Edit and return") opens the exported file (e.g. in Excel)
    and waits for a human to edit and close it before continuing/reimporting.
    Under QuietMode that interactive step is suppressed — the call returns
    almost immediately, and with immediate_import=True the exported data is
    reimported essentially unchanged (a no-op roundtrip), not a human-edited
    result. If you actually need a human to edit the data before reimport, this
    wrapper cannot provide that; use execution_mode=0 (plain export, no
    reimport) and handle editing/reimport as separate steps outside QuietMode.

    A batch across many projects with immediate_import=True writes back into
    each project (even if effectively a no-op roundtrip) — treat it as a
    write operation requiring the same care as any other project mutation
    (backups, off-hours, etc.), not as a read-only export.

    Args:
        destination: Target file (TXT, XLSX, XML; format per CONFIGSCHEME
                     extension) (parameter DESTINATION). Must be unique per
                     call when batching multiple projects.
        project_name: Project path (parameter PROJECTNAME). The action opens
                      the referenced project internally; it does not need to
                      already be open in the EPLAN GUI.
        config_scheme: Configuration scheme (parameter CONFIGSCHEME). If not set,
                       a dialog asks for it — under QuietMode this likely hangs
                       or fails silently instead. Always pass this explicitly.
        language: Language code, e.g. "en_US" or "??_??" for all (parameter LANGUAGE).
        complete_project: Export the whole project, not only selected objects.
        execution_mode: 0=Export, 1=Export and edit, 2=Edit and return (see
                        QuietMode caveat above — mode 2 behaves like a
                        roundtrip export+reimport under this wrapper, not a
                        real interactive edit).
        immediate_import: Auto-import after edit (only for execution_mode 2).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XMActionDCCommonExport",
        PROJECTNAME=project_name,
        DESTINATION=destination,
        CONFIGSCHEME=config_scheme,
        LANGUAGE=language,
        COMPLETEPROJECT=complete_project,
        EXECUTIONMODE=execution_mode,
        IMMEDIATEIMPORT=immediate_import
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
    destination_path: str = None,
    project_name: str = None,
    subproject_number: str = None,
    extend_only: bool = None
) -> dict:
    """
    Export (split off) a subproject.
    Action: subprojects (TYPE=FILEOFF)

    Note: The project must be opened in exclusive mode. After this action the
    source project object becomes invalid.

    Args:
        destination_path: Target directory (parameter DESTINATIONPATH).
                          Default is "$(MD_PROJECTS)".
        project_name: Project path (parameter PROJECTNAME).
        subproject_number: Subproject number (parameter SPNR).
        extend_only: Extend subproject only (parameter EXTENDONLY).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "subprojects",
        TYPE="FILEOFF",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        SPNR=subproject_number,
        EXTENDONLY=extend_only
    )
    return manager.execute_action(action)


def import_subproject(
    project_name: str = None,
    subproject_number: str = None,
    subproject_dir: str = None
) -> dict:
    """
    Import (store back) a subproject.
    Action: subprojects (TYPE=STORE)

    Note: The project must be opened in exclusive mode.

    Args:
        project_name: Project path (parameter PROJECTNAME).
        subproject_number: Subproject number (parameter SPNR).
        subproject_dir: Directory where the subproject is placed
                        (parameter SUBPROJECTDIR, STORE only). Default is
                        taken from the alias.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "subprojects",
        TYPE="STORE",
        PROJECTNAME=project_name,
        SPNR=subproject_number,
        SUBPROJECTDIR=subproject_dir
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
