"""
Project management actions.
"""

from typing import List
from ._base import _get_connected_manager, _build_action


def open_project(project_path: str, open_mode: str = None) -> dict:
    """
    Open a project in EPLAN.
    Action: ProjectOpen

    Args:
        project_path: Full path to the project file (.elk)
        open_mode: Optional - "Standard", "ReadOnly", or "Exclusive"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action("ProjectOpen", Project=project_path, OpenMode=open_mode)
    return manager.execute_action(action)


def close_project() -> dict:
    """
    Close the currently open project in EPLAN.
    Action: XPrjActionProjectClose
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("XPrjActionProjectClose")


def project_management(
    type: str,
    project_name: str = None,
    filename: str = None,
    scheme: str = None,
    overwrite: bool = None,
    extended_mode: bool = None,
    projects_directory: str = None,
    scan_subdirectories: bool = None
) -> dict:
    """
    Project management operations.
    Action: projectmanagement

    Args:
        type: Task type - "READPROJECTINFO", "PUBLISHSMARTPRODUCTION", "CREATESNAPSHOTCOPY",
              "EXPORTPROPERTYPLACEMENTSSCHEMAS", "IMPORTPROPERTYPLACEMENTSSCHEMAS",
              "REORGANIZE", "CORRECTPROJECTITEMS", "LOADDIRECTORY"
        project_name: Project path (optional if project is selected in GUI)
        filename: XML file path for import/export operations
        scheme: Scheme name for snapshot/correct operations
        overwrite: Whether to overwrite existing schemes (0/1)
        extended_mode: Enable extended mode for reorganize (0/1)
        projects_directory: Directory to scan for LOADDIRECTORY
        scan_subdirectories: Scan subdirectories (0/1, default 1)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "projectmanagement",
        TYPE=type,
        PROJECTNAME=project_name,
        FILENAME=filename,
        SCHEME=scheme,
        OVERWRITE=overwrite,
        EXTENDEDMODE=extended_mode,
        PROJECTSDIRECTORY=projects_directory,
        SCANSUBDIRECTORIES=scan_subdirectories
    )
    return manager.execute_action(action)


def upgrade_projects(project_paths: List[str]) -> dict:
    """
    Upgrade projects to current database scheme version.
    Action: XPrjActionUpgradeProjects

    Args:
        project_paths: List of project paths to upgrade
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    # Build action with numbered project parameters
    parts = ["XPrjActionUpgradeProjects"]
    for i, path in enumerate(project_paths, 1):
        parts.append(f'/PROJECT{i}:"{path}"')

    return manager.execute_action(" ".join(parts))


def compress_project(project_name: str = None) -> dict:
    """
    Compress a project to reduce file size.
    Action: compress
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "compress",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def synchronize_project(project_name: str = None) -> dict:
    """
    Synchronize project data.
    Action: synchronize
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "synchronize",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def get_current_project() -> dict:
    """
    Get the current project path.
    Action: selectionset
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "selectionset",
        TYPE="CURRENTPROJECT"
    )
    return manager.execute_action(action)


def set_project_language(
    language: str,
    project_name: str = None,
    read_write: bool = True
) -> dict:
    """
    Set project language.
    Action: SetProjectLanguage
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "SetProjectLanguage",
        PROJECTNAME=project_name,
        LANGUAGE=language,
        READWRITE="1" if read_write else "0"
    )
    return manager.execute_action(action)


def switch_project_type(
    project_type: str,
    project_name: str = None
) -> dict:
    """
    Change the type of project.
    Action: SwitchProjectType
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "SwitchProjectType",
        PROJECTNAME=project_name,
        PROJECTTYPE=project_type
    )
    return manager.execute_action(action)
