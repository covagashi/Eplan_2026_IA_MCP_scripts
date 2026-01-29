"""
EPLAN Actions
Complete collection of EPLAN API actions for MCP server.

All actions follow the EPLAN Remote API pattern:
- Actions are executed via execute_action() with command-line style parameters
- Parameters use /PARAM:value format
- String values with spaces should be quoted
"""

from typing import Optional, List
from eplan_connection import get_manager

TARGET_VERSION = "2026"


def _get_connected_manager():
    """Get the connection manager, ensuring it's connected."""
    manager = get_manager(TARGET_VERSION)
    if not manager.connected:
        return None, {"success": False, "message": "Not connected to EPLAN. Call eplan_connect() first."}
    return manager, None


def _build_action(action_name: str, **params) -> str:
    """Build an action string with parameters."""
    parts = [action_name]
    for key, value in params.items():
        if value is not None and value != "":
            if isinstance(value, bool):
                value = "1" if value else "0"
            # Quote strings with spaces
            if isinstance(value, str) and " " in value and not value.startswith('"'):
                value = f'"{value}"'
            parts.append(f"/{key}:{value}")
    return " ".join(parts)


# ============================================================================
# PROJECT MANAGEMENT
# ============================================================================

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


# ============================================================================
# BACKUP & RESTORE
# ============================================================================

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


# ============================================================================
# EXPORT
# ============================================================================

def export_pdf_project(
    export_file: str,
    project_name: str = None,
    export_scheme: str = None,
    black_white: int = 0,
    language: str = None,
    use_zoom: bool = False,
    zoom_level: int = None,
    fast_web_view: bool = False,
    read_only: bool = False
) -> dict:
    """
    Export project to PDF format.
    Action: export

    Args:
        export_file: Output PDF file path
        project_name: Project path (optional)
        export_scheme: PDF export scheme name
        black_white: 0=Color, 1=B&W, 2=Grayscale, 3=White Inverted
        language: Language code (e.g., "en_US")
        use_zoom: Enable zoom window for navigation
        zoom_level: Zoom level in mm (1-3500)
        fast_web_view: Enable fast web display
        read_only: Make PDF write-protected
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export",
        TYPE="PDFPROJECTSCHEME",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file,
        EXPORTSCHEME=export_scheme,
        BLACKWHITE=black_white,
        LANGUAGE=language,
        USEZOOM=use_zoom,
        ZOOMLEVEL=zoom_level,
        FASTWEBVIEW=fast_web_view,
        READONLYEXPORT=read_only
    )
    return manager.execute_action(action)


def export_pdf_pages(
    export_file: str,
    page_names: List[str],
    project_name: str = None,
    export_scheme: str = None,
    black_white: int = 0,
    language: str = None
) -> dict:
    """
    Export specific pages to PDF format.
    Action: export

    Args:
        export_file: Output PDF file path
        page_names: List of page names to export
        project_name: Project path (optional)
        export_scheme: PDF export scheme name
        black_white: 0=Color, 1=B&W, 2=Grayscale
        language: Language code
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    parts = ["export", f"/TYPE:PDFPAGESSCHEME", f'/EXPORTFILE:"{export_file}"']
    if project_name:
        parts.append(f'/PROJECTNAME:"{project_name}"')
    if export_scheme:
        parts.append(f'/EXPORTSCHEME:"{export_scheme}"')
    parts.append(f"/BLACKWHITE:{black_white}")
    if language:
        parts.append(f"/LANGUAGE:{language}")

    for i, page in enumerate(page_names, 1):
        parts.append(f"/PAGENAME{i}:{page}")

    return manager.execute_action(" ".join(parts))


def export_dxf_project(
    destination_path: str,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None
) -> dict:
    """
    Export project to DXF format.
    Action: export

    Args:
        destination_path: Output directory
        project_name: Project path (optional)
        export_scheme: DXF export scheme
        language: Language code
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export",
        TYPE="DXFPROJECT",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        EXPORTSCHEME=export_scheme,
        LANGUAGE=language
    )
    return manager.execute_action(action)


def export_dwg_project(
    destination_path: str,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None
) -> dict:
    """
    Export project to DWG format.
    Action: export

    Args:
        destination_path: Output directory
        project_name: Project path (optional)
        export_scheme: DWG export scheme
        language: Language code
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export",
        TYPE="DWGPROJECT",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        EXPORTSCHEME=export_scheme,
        LANGUAGE=language
    )
    return manager.execute_action(action)


def export_graphics_project(
    destination_path: str,
    project_name: str = None,
    format: str = "PNG",
    color_depth: int = 24,
    image_width: int = 1024,
    black_white: bool = False,
    compression: str = "NONE"
) -> dict:
    """
    Export project to graphical format (PNG, TIF, GIF, JPG, BMP).
    Action: export

    Args:
        destination_path: Output directory
        project_name: Project path (optional)
        format: Image format - "PNG", "TIF", "GIF", "JPG", "BMP"
        color_depth: 1, 8, 16, 24, or 32
        image_width: Image width in pixels
        black_white: Black and white output
        compression: For TIF - "LZW", "RLE", "CCITT3", "CCITT4", "NONE"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export",
        TYPE="GRAPHICPROJECT",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        FORMAT=format,
        COLORDEPTH=color_depth,
        IMAGEWIDTH=image_width,
        BLACKWHITE=black_white,
        IMAGECOMPRESSION=compression
    )
    return manager.execute_action(action)


def export_pxf_project(
    export_file: str,
    project_name: str = None,
    export_masterdata: bool = True,
    export_connections: bool = False
) -> dict:
    """
    Export project in EPJ/PXF format.
    Action: export

    Args:
        export_file: Output file path
        project_name: Project path (optional)
        export_masterdata: Include master data
        export_connections: Include connections
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export",
        TYPE="PXFPROJECT",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file,
        EXPORTMASTERDATA=export_masterdata,
        EXPORTCONNECTIONS=export_connections
    )
    return manager.execute_action(action)


def export_3d(
    destination_path: str,
    project_name: str = None,
    format: str = None,
    installation_space: str = None
) -> dict:
    """
    Export installation spaces to 3D formats.
    Action: export3d

    Args:
        destination_path: Output directory
        project_name: Project path (optional)
        format: 3D export format
        installation_space: Specific installation space to export
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export3d",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        FORMAT=format,
        INSTALLATIONSPACE=installation_space
    )
    return manager.execute_action(action)


# ============================================================================
# IMPORT
# ============================================================================

def import_pxf_project(
    import_file: str,
    project_name: str,
    balance_articles: bool = False,
    generate_auto_cables: bool = False,
    verify: bool = False
) -> dict:
    """
    Import a PXF/EPJ project.
    Action: import

    Args:
        import_file: Path to PXF file
        project_name: Target project path
        balance_articles: Sync parts with database
        generate_auto_cables: Generate automatic cables
        verify: Run project check after import
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "import",
        TYPE="PXFPROJECT",
        IMPORTFILE=import_file,
        PROJECTNAME=project_name,
        BALANCEARTICLES=balance_articles,
        GENERATEAUTOMATICCABLES=generate_auto_cables,
        VERIFY=verify
    )
    return manager.execute_action(action)


def import_dwg_page(
    import_file: str,
    page_name: str,
    project_name: str = None,
    import_scheme: str = None,
    x_scale: float = 1.0,
    y_scale: float = 1.0,
    x_offset: float = 0.0,
    y_offset: float = 0.0
) -> dict:
    """
    Insert DWG drawing into a page.
    Action: import

    Args:
        import_file: Path to DWG file
        page_name: Target page name
        project_name: Project path (optional)
        import_scheme: DWG import scheme
        x_scale: X scaling factor
        y_scale: Y scaling factor
        x_offset: X offset
        y_offset: Y offset
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "import",
        TYPE="DWGPAGE",
        IMPORTFILE=import_file,
        PAGENAME=page_name,
        PROJECTNAME=project_name,
        IMPORTSCHEME=import_scheme,
        XSCALE=x_scale,
        YSCALE=y_scale,
        XOFFSET=x_offset,
        YOFFSET=y_offset
    )
    return manager.execute_action(action)


def import_dxf_page(
    import_file: str,
    page_name: str,
    project_name: str = None,
    import_scheme: str = None,
    x_scale: float = 1.0,
    y_scale: float = 1.0,
    x_offset: float = 0.0,
    y_offset: float = 0.0
) -> dict:
    """
    Insert DXF drawing into a page.
    Action: import
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "import",
        TYPE="DXFPAGE",
        IMPORTFILE=import_file,
        PAGENAME=page_name,
        PROJECTNAME=project_name,
        IMPORTSCHEME=import_scheme,
        XSCALE=x_scale,
        YSCALE=y_scale,
        XOFFSET=x_offset,
        YOFFSET=y_offset
    )
    return manager.execute_action(action)


def import_3d(
    import_file: str,
    project_name: str = None,
    import_scheme: str = None
) -> dict:
    """
    Import 3D data.
    Action: import3d
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "import3d",
        IMPORTFILE=import_file,
        PROJECTNAME=project_name,
        IMPORTSCHEME=import_scheme
    )
    return manager.execute_action(action)


# ============================================================================
# PRINT
# ============================================================================

def print_project(
    project_name: str = None,
    printer_name: str = None,
    copies: int = 1,
    collate: bool = True,
    reverse: bool = False,
    destination_file: str = None
) -> dict:
    """
    Print a project.
    Action: print

    Args:
        project_name: Project path (optional)
        printer_name: Printer name (optional, uses default)
        copies: Number of copies
        collate: Sorted order
        reverse: Reverse order
        destination_file: Output to file instead of printer
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "print",
        TYPE="PROJECT",
        PROJECTNAME=project_name,
        PRINTERNAME=printer_name,
        NUMBER=copies,
        PRINTCOLLATE=collate,
        PRINTREVERSE=reverse,
        DESTINATIONFILE=destination_file
    )
    return manager.execute_action(action)


def print_pages(
    page_name: str = None,
    project_name: str = None,
    printer_name: str = None,
    copies: int = 1,
    use_page_filter: bool = False,
    print_changed_only: bool = False
) -> dict:
    """
    Print specific pages.
    Action: print

    Args:
        page_name: Page name to print (optional)
        project_name: Project path (optional)
        printer_name: Printer name
        copies: Number of copies
        use_page_filter: Use active page filter
        print_changed_only: Print only changed pages
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "print",
        TYPE="PAGES",
        PAGENAME=page_name,
        PROJECTNAME=project_name,
        PRINTERNAME=printer_name,
        NUMBER=copies,
        USEPAGEFILTER=use_page_filter,
        PRINTCHANGEDPAGES=print_changed_only
    )
    return manager.execute_action(action)


# ============================================================================
# CHECK / VERIFY
# ============================================================================

def check_project(
    project_name: str = None,
    verification_scheme: str = None,
    verify_completed_only: bool = False
) -> dict:
    """
    Check/verify a project.
    Action: check

    Args:
        project_name: Project path (optional)
        verification_scheme: Verification scheme name
        verify_completed_only: Check completed messages only
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "check",
        TYPE="PROJECT",
        PROJECTNAME=project_name,
        VERIFICATIONSCHEME=verification_scheme,
        VERIFYCOMPLETEDONLY=verify_completed_only
    )
    return manager.execute_action(action)


def check_pages(
    page_name: str = None,
    project_name: str = None,
    verification_scheme: str = None,
    use_page_filter: bool = False
) -> dict:
    """
    Check specific pages.
    Action: check
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "check",
        TYPE="PAGES",
        PAGENAME=page_name,
        PROJECTNAME=project_name,
        VERIFICATIONSCHEME=verification_scheme,
        USEPAGEFILTER=use_page_filter
    )
    return manager.execute_action(action)


def check_parts(
    verification_scheme: str = None,
    verify_completed_only: bool = False
) -> dict:
    """
    Check parts in the database.
    Action: check
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "check",
        TYPE="PARTS",
        VERIFICATIONSCHEME=verification_scheme,
        VERIFYCOMPLETEDONLY=verify_completed_only
    )
    return manager.execute_action(action)


# ============================================================================
# GENERATE
# ============================================================================

def generate_connections(
    project_name: str = None,
    page_name: str = None,
    rebuild_all: bool = False,
    use_page_filter: bool = False
) -> dict:
    """
    Generate connections in project.
    Action: generate

    Args:
        project_name: Project path (optional)
        page_name: Specific page (optional)
        rebuild_all: Rebuild all connections vs update only
        use_page_filter: Use active page filter
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "generate",
        TYPE="CONNECTIONS",
        PROJECTNAME=project_name,
        PAGENAME=page_name,
        REBUILDALLCONNECTIONS=rebuild_all,
        USEPAGEFILTER=use_page_filter
    )
    return manager.execute_action(action)


def generate_cables(
    project_name: str = None,
    creation_scheme: str = None,
    numbering_scheme: str = None,
    autoselect_scheme: str = None,
    keep_old_names: bool = True,
    start_value: int = 1,
    step_value: int = 1,
    only_auto_cables: bool = True
) -> dict:
    """
    Generate cables in project.
    Action: generate

    Args:
        project_name: Project path (optional)
        creation_scheme: Cable creation scheme
        numbering_scheme: Cable numbering scheme
        autoselect_scheme: Auto cable selection scheme
        keep_old_names: Preserve existing cable names
        start_value: Start value for DT counter
        step_value: Increment value
        only_auto_cables: Only select for auto cables
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "generate",
        TYPE="CABLES",
        PROJECTNAME=project_name,
        CREATIONSCHEME=creation_scheme,
        NUMBERINGSCHEME=numbering_scheme,
        AUTOSELECTSCHEME=autoselect_scheme,
        KEEPOLDNAMES=keep_old_names,
        STARTVALUE=start_value,
        STEPVALUE=step_value,
        ONLYAUTOCABLES=only_auto_cables
    )
    return manager.execute_action(action)


# ============================================================================
# REPORTS
# ============================================================================

def update_reports(
    project_name: str = None,
    page_name: str = None,
    use_page_filter: bool = False
) -> dict:
    """
    Update project reports/evaluations.
    Action: reports

    Args:
        project_name: Project path (optional)
        page_name: Specific page to update
        use_page_filter: Use active page filter
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "reports",
        TYPE="PROJECT" if not page_name else "PAGES",
        PROJECTNAME=project_name,
        PAGENAME=page_name,
        USEPAGEFILTER=use_page_filter
    )
    return manager.execute_action(action)


def create_model_views(
    project_name: str = None,
    templates: List[str] = None,
    replace_existing: bool = False
) -> dict:
    """
    Create model views.
    Action: reports
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    parts = ["reports", "/TYPE:CREATEMODELVIEWS"]
    if project_name:
        parts.append(f'/PROJECTNAME:"{project_name}"')
    if templates:
        for i, t in enumerate(templates, 1):
            parts.append(f'/TEMPLATE{i}:"{t}"')
    if replace_existing:
        parts.append("/REPLACEEXISTING:1")

    return manager.execute_action(" ".join(parts))


# ============================================================================
# SEARCH
# ============================================================================

def search_devices(
    search_item: str,
    project_name: str = None,
    case_sensitive: bool = False,
    whole_text: bool = False
) -> dict:
    """
    Search for devices in project.
    Action: search
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "search",
        TYPE="DEVICETAG",
        SEARCHITEM=search_item,
        PROJECTNAME=project_name,
        CASESENSITIVE=case_sensitive,
        WHOLETEXT=whole_text
    )
    return manager.execute_action(action)


def search_text(
    search_item: str,
    project_name: str = None,
    case_sensitive: bool = False,
    whole_text: bool = False,
    logic_pages: bool = True,
    graphic_pages: bool = True,
    evaluation_pages: bool = True
) -> dict:
    """
    Search for text in project.
    Action: search
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "search",
        TYPE="TEXTS",
        SEARCHITEM=search_item,
        PROJECTNAME=project_name,
        CASESENSITIVE=case_sensitive,
        WHOLETEXT=whole_text,
        LOGICPAGES=logic_pages,
        GRAPHICPAGES=graphic_pages,
        EVALUATIONPAGES=evaluation_pages
    )
    return manager.execute_action(action)


def search_all_properties(
    search_item: str,
    project_name: str = None,
    case_sensitive: bool = False
) -> dict:
    """
    Search through all properties in project.
    Action: search
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "search",
        TYPE="ALLPROPERTIES",
        SEARCHITEM=search_item,
        PROJECTNAME=project_name,
        CASESENSITIVE=case_sensitive
    )
    return manager.execute_action(action)


# ============================================================================
# EDIT / NAVIGATION
# ============================================================================

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


# ============================================================================
# RENUMBER
# ============================================================================

def renumber_devices(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    config_scheme: str = None,
    filter_scheme: str = None,
    identifier: str = None,
    use_selection: bool = False,
    post_numerate: bool = True,
    numerate_cables: bool = False
) -> dict:
    """
    Renumber devices in project.
    Action: renumber
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "renumber",
        TYPE="DEVICES",
        PROJECTNAME=project_name,
        STARTVALUE=start_value,
        STEPVALUE=step_value,
        CONFIGSCHEME=config_scheme,
        FILTERSCHEME=filter_scheme,
        IDENTIFIER=identifier,
        USESELECTION=use_selection,
        POSTNUMERATE=post_numerate,
        NUMERATECABLES=numerate_cables
    )
    return manager.execute_action(action)


def renumber_pages(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    structure_oriented: bool = False,
    keep_interval: bool = False,
    keep_text: bool = False,
    use_selection: bool = False
) -> dict:
    """
    Renumber pages in project.
    Action: renumber
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "renumber",
        TYPE="PAGES",
        PROJECTNAME=project_name,
        STARTVALUE=start_value,
        STEPVALUE=step_value,
        STRUCTUREORIENTED=structure_oriented,
        KEEPINTERVAL=keep_interval,
        KEEPTEXT=keep_text,
        USESELECTION=use_selection
    )
    return manager.execute_action(action)


def renumber_cables(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    config_scheme: str = None,
    use_selection: bool = False,
    keep_existing: bool = False,
    keep_identifier: bool = False
) -> dict:
    """
    Renumber cables in project.
    Action: renumber
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "renumber",
        TYPE="CABLES",
        PROJECTNAME=project_name,
        STARTVALUE=start_value,
        STEPVALUE=step_value,
        CONFIGSCHEME=config_scheme,
        USESELECTION=use_selection,
        KEEPEXISTING=keep_existing,
        KEEPIDENTIFIER=keep_identifier
    )
    return manager.execute_action(action)


def renumber_terminals(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    config_scheme: str = None,
    use_selection: bool = False,
    sequence: int = 0,
    prefix: str = None,
    suffix: str = None
) -> dict:
    """
    Renumber terminals in project.
    Action: renumber

    Args:
        sequence: 0=Like sorting, 1=Page oriented, 2=Cable oriented, 3=Level oriented
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "renumber",
        TYPE="TERMINALS",
        PROJECTNAME=project_name,
        STARTVALUE=start_value,
        STEPVALUE=step_value,
        CONFIGSCHEME=config_scheme,
        USESELECTION=use_selection,
        SEQUENCE=sequence,
        PREFIX=prefix,
        SUFFIX=suffix
    )
    return manager.execute_action(action)


# ============================================================================
# TRANSLATE
# ============================================================================

def translate_project(project_name: str = None) -> dict:
    """
    Translate a project using the translation database.
    Action: translate
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "translate",
        TYPE="TRANSLATEPROJECT",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def export_missing_translations(
    export_file: str,
    language: str,
    project_name: str = None,
    converter: str = None
) -> dict:
    """
    Export missing translations list.
    Action: translate
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "translate",
        TYPE="EXPORTMISSINGTRANSLATIONS",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file,
        LANGUAGE=language,
        CONVERTER=converter
    )
    return manager.execute_action(action)


def remove_language(language: str, project_name: str = None) -> dict:
    """
    Remove a language from project.
    Action: translate

    Args:
        language: Language code(s) to remove (e.g., "en_US" or "en_US,fr_FR")
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "translate",
        TYPE="REMOVELANGUAGE",
        PROJECTNAME=project_name,
        LANGUAGE=language
    )
    return manager.execute_action(action)


# ============================================================================
# DEVICE LIST
# ============================================================================

def export_device_list(
    export_file: str,
    project_name: str = None,
    format: str = "XDLXmlExporter"
) -> dict:
    """
    Export device list from project.
    Action: devicelist

    Args:
        export_file: Output file path
        project_name: Project path (optional)
        format: Export format - "XDLXmlExporter", "XDLTxtImporterExporter", "XDLCsvImporterExporter"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "devicelist",
        TYPE="EXPORT",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file,
        FORMAT=format
    )
    return manager.execute_action(action)


def import_device_list(
    import_file: str,
    project_name: str = None,
    format: str = "XDLXmlExporter"
) -> dict:
    """
    Import device list into project.
    Action: devicelist
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "devicelist",
        TYPE="IMPORT",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file,
        FORMAT=format
    )
    return manager.execute_action(action)


def delete_device_list(project_name: str = None) -> dict:
    """
    Delete device list from project.
    Action: devicelist
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "devicelist",
        TYPE="DELETE",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


# ============================================================================
# LABELING
# ============================================================================

def create_labels(
    destination_file: str,
    project_name: str = None,
    config_scheme: str = None,
    filter_scheme: str = None,
    sort_scheme: str = None,
    language: str = None,
    record_repeat: int = None,
    task_repeat: int = None,
    show_output: bool = False,
    use_selection: bool = False
) -> dict:
    """
    Create labels for project.
    Action: label

    Args:
        destination_file: Output file (txt, xls, xlsx, xml)
        project_name: Project path (optional)
        config_scheme: Configuration scheme
        filter_scheme: Filter scheme
        sort_scheme: Sorting scheme
        language: Language code
        record_repeat: Repetitions per label
        task_repeat: Repetitions of total output
        show_output: Show output file after generation
        use_selection: Use current selection as input
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "label",
        PROJECTNAME=project_name,
        DESTINATIONFILE=destination_file,
        CONFIGSCHEME=config_scheme,
        FILTERSCHEME=filter_scheme,
        SORTSCHEME=sort_scheme,
        LANGUAGE=language,
        RECREPEAT=record_repeat,
        TASKREPEAT=task_repeat,
        SHOWOUTPUT=show_output,
        USESELECTION=use_selection
    )
    return manager.execute_action(action)


# ============================================================================
# COMPRESS
# ============================================================================

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


# ============================================================================
# LAYER MANAGEMENT
# ============================================================================

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


# ============================================================================
# MACROS
# ============================================================================

def generate_macros(
    project_name: str = None,
    destination_path: str = None,
    scheme: str = None
) -> dict:
    """
    Generate macros from project.
    Action: generatemacros
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "generatemacros",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        SCHEME=scheme
    )
    return manager.execute_action(action)


def prepare_macros(project_name: str = None) -> dict:
    """
    Prepare project for macro generation.
    Action: preparemacros
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "preparemacros",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def update_macros(project_path: str = None) -> dict:
    """
    Update macros in project.
    Action: XGedUpdateMacroAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XGedUpdateMacroAction",
        PROJECTPATH=project_path
    )
    return manager.execute_action(action)


# ============================================================================
# SCRIPTS
# ============================================================================

def register_script(script_file: str) -> dict:
    """
    Register a script in EPLAN.
    Action: RegisterScript
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "RegisterScript",
        ScriptFile=script_file
    )
    return manager.execute_action(action)


def unregister_script(script_file: str) -> dict:
    """
    Unregister a script from EPLAN.
    Action: UnregisterScript
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "UnregisterScript",
        ScriptFile=script_file
    )
    return manager.execute_action(action)


def execute_script(script_file: str) -> dict:
    """
    Execute a registered script.
    Action: ExecuteScript
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ExecuteScript",
        ScriptFile=script_file
    )
    return manager.execute_action(action)


# ============================================================================
# SETTINGS
# ============================================================================

def export_settings(
    export_file: str,
    setting_type: str = None
) -> dict:
    """
    Export settings to XML file.
    Action: XSettingsExport
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsExport",
        EXPORTFILE=export_file,
        SETTINGTYPE=setting_type
    )
    return manager.execute_action(action)


def import_settings(
    import_file: str,
    setting_type: str = None
) -> dict:
    """
    Import settings from XML file.
    Action: XSettingsImport
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsImport",
        IMPORTFILE=import_file,
        SETTINGTYPE=setting_type
    )
    return manager.execute_action(action)


def set_setting(name: str, value: str) -> dict:
    """
    Set a setting value.
    Action: XAfActionSetting
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XAfActionSetting",
        NAME=name,
        VALUE=value
    )
    return manager.execute_action(action)


def set_project_setting(name: str, value: str, project_name: str = None) -> dict:
    """
    Set a project setting value.
    Action: XAfActionSettingProject
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XAfActionSettingProject",
        PROJECTNAME=project_name,
        NAME=name,
        VALUE=value
    )
    return manager.execute_action(action)


# ============================================================================
# PROPERTIES
# ============================================================================

def get_project_property(property_id: str, project_name: str = None) -> dict:
    """
    Get a property value from the project.
    Action: XEsGetProjectPropertyAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XEsGetProjectPropertyAction",
        PROJECTNAME=project_name,
        PROPERTYID=property_id
    )
    return manager.execute_action(action)


def set_project_property(property_id: str, value: str, project_name: str = None) -> dict:
    """
    Set a property value on the project.
    Action: XEsSetProjectPropertyAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XEsSetProjectPropertyAction",
        PROJECTNAME=project_name,
        PROPERTYID=property_id,
        VALUE=value
    )
    return manager.execute_action(action)


def get_page_property(property_id: str, page_name: str = None) -> dict:
    """
    Get a property value from the first selected page.
    Action: XEsGetPagePropertyAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XEsGetPagePropertyAction",
        PAGENAME=page_name,
        PROPERTYID=property_id
    )
    return manager.execute_action(action)


def set_page_property(property_id: str, value: str, page_name: str = None) -> dict:
    """
    Set a property value on selected pages.
    Action: XEsSetPagePropertyAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XEsSetPagePropertyAction",
        PAGENAME=page_name,
        PROPERTYID=property_id,
        VALUE=value
    )
    return manager.execute_action(action)


def export_user_properties(export_file: str, project_name: str = None) -> dict:
    """
    Export user properties to file.
    Action: XEsUserPropertiesExportAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XEsUserPropertiesExportAction",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def import_user_properties(import_file: str, project_name: str = None) -> dict:
    """
    Import user properties from file.
    Action: XEsUserPropertiesImportAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XEsUserPropertiesImportAction",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)


# ============================================================================
# PARTS MANAGEMENT
# ============================================================================

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


# ============================================================================
# PLC
# ============================================================================

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


# ============================================================================
# WORKSPACE
# ============================================================================

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


# ============================================================================
# DATA EXCHANGE / SYNCHRONIZE
# ============================================================================

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


# ============================================================================
# CONNECTIONS
# ============================================================================

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


# ============================================================================
# SUBPROJECTS
# ============================================================================

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


# ============================================================================
# MASTER DATA
# ============================================================================

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


# ============================================================================
# RIBBON BAR
# ============================================================================

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


# ============================================================================
# 3D / CABINET
# ============================================================================

def calculate_cabinet_weight(project_name: str = None) -> dict:
    """
    Calculate total weight of cabinet.
    Action: XCabCalculateEnclosureTotalWeightAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XCabCalculateEnclosureTotalWeightAction",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def update_segments_filling(project_name: str = None) -> dict:
    """
    Calculate and set segment filling values.
    Action: UpdateSegmentsFilling
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "UpdateSegmentsFilling",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


# ============================================================================
# PROJECT LANGUAGE
# ============================================================================

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


# ============================================================================
# PROJECT TYPE
# ============================================================================

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


# ============================================================================
# SELECTION SET
# ============================================================================

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


# ============================================================================
# PREVIEW
# ============================================================================

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


# ============================================================================
# NAVIGATE TO EEC
# ============================================================================

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


# ============================================================================
# TOPOLOGY
# ============================================================================

def topology_operation(
    operation_type: str,
    project_name: str = None
) -> dict:
    """
    Perform topology-related operations.
    Action: Topology
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "Topology",
        TYPE=operation_type,
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


# ============================================================================
# IMPORT PRE-PLANNING DATA
# ============================================================================

def import_preplanning_data(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import pre-planning data.
    Action: ImportPrePlanningData
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ImportPrePlanningData",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)


# ============================================================================
# SEGMENTS
# ============================================================================

def export_segments_template(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export segment templates to file.
    Action: ExportSegmentsTemplate
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ExportSegmentsTemplate",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def import_segments_template(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import segment templates from file.
    Action: ImportSegmentsTemplate
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ImportSegmentsTemplate",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)


# ============================================================================
# NC DATA / PRODUCTION
# ============================================================================

def export_nc_data(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export NC data for machines.
    Action: ExportNCData
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ExportNCData",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def export_production_wiring(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export production wiring data for machines.
    Action: ExportProductionWiring
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ExportProductionWiring",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


# ============================================================================
# API MODULE / ADD-INS
# ============================================================================

def load_api_module(module_path: str) -> dict:
    """
    Load and register an API add-in.
    Action: EplApiModuleAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "EplApiModuleAction",
        MODULEPATH=module_path
    )
    return manager.execute_action(action)


def register_addon(addon_path: str) -> dict:
    """
    Register an add-on.
    Action: XSettingsRegisterAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsRegisterAction",
        ADDONPATH=addon_path
    )
    return manager.execute_action(action)


def unregister_addon(addon_path: str) -> dict:
    """
    Unregister an add-on.
    Action: XSettingsUnregisterAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsUnregisterAction",
        ADDONPATH=addon_path
    )
    return manager.execute_action(action)


# ============================================================================
# RAW ACTION EXECUTION
# ============================================================================

def execute_raw_action(action_string: str) -> dict:
    """
    Execute a raw EPLAN action string.
    Use this for actions not covered by specific functions.

    Args:
        action_string: Complete action string (e.g., "ActionName /PARAM1:value1 /PARAM2:value2")

    Example:
        execute_raw_action('ProjectOpen /Project:"C:\\Projects\\test.elk"')
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action(action_string)
