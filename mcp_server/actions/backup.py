"""
Backup and restore actions.
"""

from ._base import _get_connected_manager, _build_action


def backup_project(
    destination_path: str,
    archive_name: str,
    project_name: str = None,
    comment: str = None,
    auto_copy_ref_data: bool = False,
    include_ext_docs: bool = False,
    include_images: bool = False,
    backup_method: str = "BACKUP"
) -> dict:
    """
    Backup a project to disk.
    Action: backup

    Args:
        destination_path: Target directory
        archive_name: Archive filename (without path)
        project_name: Project path (optional if selected in GUI)
        comment: Backup comment
        auto_copy_ref_data: Copy referenced external files (0/1)
        include_ext_docs: Include external documents (0/1)
        include_images: Include images (0/1)
        backup_method: "BACKUP", "SOURCEOUT", or "ARCHIVE"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "backup",
        TYPE="PROJECT",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        ARCHIVENAME=archive_name,
        COMMENT=comment,
        AUTOCOPYREFDATA=auto_copy_ref_data,
        INCLEXTDOCS=include_ext_docs,
        INCLIMAGES=include_images,
        BACKUPMETHOD=backup_method
    )
    return manager.execute_action(action)


def backup_masterdata(
    destination_path: str,
    archive_name: str,
    source_path: str,
    md_type: str,
    filename: str = "*.*",
    comment: str = None
) -> dict:
    """
    Backup master data (forms, symbols, etc.) to disk.
    Action: backup

    Args:
        destination_path: Target directory
        archive_name: Archive filename
        source_path: Source directory with master data
        md_type: Master data type - "SYMBOLS", "MACROS", "FORMS", "ARTICLES",
                 "LANGUAGES", "STANDARDSHEET", "STATIONDATA"
        filename: File pattern (e.g., "*.fn1", "*.*")
        comment: Backup comment
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "backup",
        TYPE="MASTERDATA",
        DESTINATIONPATH=destination_path,
        ARCHIVENAME=archive_name,
        SOURCEPATH=source_path,
        MDTYPE=md_type,
        FILENAME=filename,
        COMMENT=comment
    )
    return manager.execute_action(action)


def restore_project(
    archive_name: str,
    project_name: str,
    unpack_project: bool = False,
    restore_project_info: bool = True
) -> dict:
    """
    Restore a project from backup.
    Action: restore

    Args:
        archive_name: Path to archive file
        project_name: Target project path
        unpack_project: Unpack previously packed project (0/1)
        restore_project_info: Restore ProjectInfo.xml (0/1)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "restore",
        TYPE="PROJECT",
        ARCHIVENAME=archive_name,
        PROJECTNAME=project_name,
        UNPACKPROJECT=unpack_project,
        MODE="1" if restore_project_info else "0"
    )
    return manager.execute_action(action)


def restore_masterdata(archive_name: str, destination_path: str) -> dict:
    """
    Restore master data from backup.
    Action: restore

    Args:
        archive_name: Path to archive file
        destination_path: Target directory
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "restore",
        TYPE="MASTERDATA",
        ARCHIVENAME=archive_name,
        DESTINATIONPATH=destination_path
    )
    return manager.execute_action(action)
