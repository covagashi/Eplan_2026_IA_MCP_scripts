"""
EPLAN MCP Server

Complete EPLAN automation server exposing all API actions via MCP protocol.

Requirements:
- EPLAN installed
- pip install pythonnet mcp
"""

import json
import os
from typing import Optional, List
from mcp.server.fastmcp import FastMCP
from eplan_connection import get_manager
import actions

TARGET_VERSION = "2025"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

mcp = FastMCP("EPLAN MCP Server")


# ============================================================================
# CONNECTION MANAGEMENT
# ============================================================================

@mcp.tool()
def eplan_status() -> str:
    """Get the current EPLAN connection status."""
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.get_status(), indent=2)


@mcp.tool()
def eplan_servers() -> str:
    """List active EPLAN servers (running instances)."""
    manager = get_manager(TARGET_VERSION)
    servers = manager.get_active_servers()
    return json.dumps({"servers": servers, "count": len(servers)}, indent=2)


@mcp.tool()
def eplan_connect(port: str = None) -> str:
    """Connect to EPLAN. Port is auto-detected if not specified."""
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.connect(port=port), indent=2)


@mcp.tool()
def eplan_disconnect() -> str:
    """Disconnect from EPLAN."""
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.disconnect(), indent=2)


@mcp.tool()
def eplan_ping() -> str:
    """Check if EPLAN is responding."""
    manager = get_manager(TARGET_VERSION)
    return json.dumps(manager.ping(), indent=2)


# ============================================================================
# PROJECT MANAGEMENT
# ============================================================================

@mcp.tool()
def eplan_open_project(project_path: str, open_mode: str = None) -> str:
    """
    Open a project in EPLAN.

    Args:
        project_path: Full path to the project file (.elk)
        open_mode: Optional - "Standard", "ReadOnly", or "Exclusive"
    """
    return json.dumps(actions.open_project(project_path, open_mode), indent=2)


@mcp.tool()
def eplan_close_project() -> str:
    """Close the currently open project."""
    return json.dumps(actions.close_project(), indent=2)


@mcp.tool()
def eplan_project_management(
    type: str,
    project_name: str = None,
    filename: str = None,
    scheme: str = None,
    overwrite: bool = None,
    extended_mode: bool = None,
    projects_directory: str = None,
    scan_subdirectories: bool = None
) -> str:
    """
    Project management operations.

    Args:
        type: Task type - "READPROJECTINFO", "PUBLISHSMARTPRODUCTION", "CREATESNAPSHOTCOPY",
              "EXPORTPROPERTYPLACEMENTSSCHEMAS", "IMPORTPROPERTYPLACEMENTSSCHEMAS",
              "REORGANIZE", "CORRECTPROJECTITEMS", "LOADDIRECTORY"
        project_name: Project path (optional if project is selected in GUI)
        filename: XML file path for import/export operations
        scheme: Scheme name for snapshot/correct operations
        overwrite: Whether to overwrite existing schemes
        extended_mode: Enable extended mode for reorganize
        projects_directory: Directory to scan for LOADDIRECTORY
        scan_subdirectories: Scan subdirectories (default True)
    """
    return json.dumps(actions.project_management(
        type, project_name, filename, scheme, overwrite,
        extended_mode, projects_directory, scan_subdirectories
    ), indent=2)


# ============================================================================
# BACKUP & RESTORE
# ============================================================================

@mcp.tool()
def eplan_backup_project(
    destination_path: str,
    archive_name: str,
    project_name: str = None,
    comment: str = None,
    auto_copy_ref_data: bool = False,
    include_ext_docs: bool = False,
    include_images: bool = False,
    backup_method: str = "BACKUP"
) -> str:
    """
    Backup a project to disk.

    Args:
        destination_path: Target directory
        archive_name: Archive filename (without path)
        project_name: Project path (optional if selected in GUI)
        comment: Backup comment
        auto_copy_ref_data: Copy referenced external files
        include_ext_docs: Include external documents
        include_images: Include images
        backup_method: "BACKUP", "SOURCEOUT", or "ARCHIVE"
    """
    return json.dumps(actions.backup_project(
        destination_path, archive_name, project_name, comment,
        auto_copy_ref_data, include_ext_docs, include_images, backup_method
    ), indent=2)


@mcp.tool()
def eplan_backup_masterdata(
    destination_path: str,
    archive_name: str,
    source_path: str,
    md_type: str,
    filename: str = "*.*",
    comment: str = None
) -> str:
    """
    Backup master data (forms, symbols, etc.) to disk.

    Args:
        destination_path: Target directory
        archive_name: Archive filename
        source_path: Source directory with master data
        md_type: "SYMBOLS", "MACROS", "FORMS", "ARTICLES", "LANGUAGES", "STANDARDSHEET", "STATIONDATA"
        filename: File pattern (e.g., "*.fn1", "*.*")
        comment: Backup comment
    """
    return json.dumps(actions.backup_masterdata(
        destination_path, archive_name, source_path, md_type, filename, comment
    ), indent=2)


@mcp.tool()
def eplan_restore_project(
    archive_name: str,
    project_name: str,
    unpack_project: bool = False,
    restore_project_info: bool = True
) -> str:
    """
    Restore a project from backup.

    Args:
        archive_name: Path to archive file
        project_name: Target project path
        unpack_project: Unpack previously packed project
        restore_project_info: Restore ProjectInfo.xml
    """
    return json.dumps(actions.restore_project(
        archive_name, project_name, unpack_project, restore_project_info
    ), indent=2)


@mcp.tool()
def eplan_restore_masterdata(archive_name: str, destination_path: str) -> str:
    """
    Restore master data from backup.

    Args:
        archive_name: Path to archive file
        destination_path: Target directory
    """
    return json.dumps(actions.restore_masterdata(archive_name, destination_path), indent=2)


# ============================================================================
# EXPORT
# ============================================================================

@mcp.tool()
def eplan_export_pdf_project(
    export_file: str,
    project_name: str = None,
    export_scheme: str = None,
    black_white: int = 0,
    language: str = None,
    use_zoom: bool = False,
    zoom_level: int = None,
    fast_web_view: bool = False,
    read_only: bool = False
) -> str:
    """
    Export project to PDF format.

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
    return json.dumps(actions.export_pdf_project(
        export_file, project_name, export_scheme, black_white,
        language, use_zoom, zoom_level, fast_web_view, read_only
    ), indent=2)


@mcp.tool()
def eplan_export_pdf_pages(
    export_file: str,
    page_names: List[str],
    project_name: str = None,
    export_scheme: str = None,
    black_white: int = 0,
    language: str = None
) -> str:
    """
    Export specific pages to PDF format.

    Args:
        export_file: Output PDF file path
        page_names: List of page names to export (e.g., ["=AP+ST1/2", "=AP+ST1/4"])
        project_name: Project path (optional)
        export_scheme: PDF export scheme name
        black_white: 0=Color, 1=B&W, 2=Grayscale
        language: Language code
    """
    return json.dumps(actions.export_pdf_pages(
        export_file, page_names, project_name, export_scheme, black_white, language
    ), indent=2)


@mcp.tool()
def eplan_export_dxf_project(
    destination_path: str,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None
) -> str:
    """Export project to DXF format."""
    return json.dumps(actions.export_dxf_project(
        destination_path, project_name, export_scheme, language
    ), indent=2)


@mcp.tool()
def eplan_export_dwg_project(
    destination_path: str,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None
) -> str:
    """Export project to DWG format."""
    return json.dumps(actions.export_dwg_project(
        destination_path, project_name, export_scheme, language
    ), indent=2)


@mcp.tool()
def eplan_export_graphics_project(
    destination_path: str,
    project_name: str = None,
    format: str = "PNG",
    color_depth: int = 24,
    image_width: int = 1024,
    black_white: bool = False,
    compression: str = "NONE"
) -> str:
    """
    Export project to graphical format.

    Args:
        destination_path: Output directory
        project_name: Project path (optional)
        format: "PNG", "TIF", "GIF", "JPG", "BMP"
        color_depth: 1, 8, 16, 24, or 32
        image_width: Image width in pixels
        black_white: Black and white output
        compression: For TIF - "LZW", "RLE", "CCITT3", "CCITT4", "NONE"
    """
    return json.dumps(actions.export_graphics_project(
        destination_path, project_name, format, color_depth,
        image_width, black_white, compression
    ), indent=2)


@mcp.tool()
def eplan_export_pxf_project(
    export_file: str,
    project_name: str = None,
    export_masterdata: bool = True,
    export_connections: bool = False
) -> str:
    """Export project in EPJ/PXF format for exchange."""
    return json.dumps(actions.export_pxf_project(
        export_file, project_name, export_masterdata, export_connections
    ), indent=2)


@mcp.tool()
def eplan_export_3d(
    destination_path: str,
    project_name: str = None,
    format: str = None,
    installation_space: str = None
) -> str:
    """Export installation spaces to 3D formats."""
    return json.dumps(actions.export_3d(
        destination_path, project_name, format, installation_space
    ), indent=2)


# ============================================================================
# IMPORT
# ============================================================================

@mcp.tool()
def eplan_import_pxf_project(
    import_file: str,
    project_name: str,
    balance_articles: bool = False,
    generate_auto_cables: bool = False,
    verify: bool = False
) -> str:
    """
    Import a PXF/EPJ project.

    Args:
        import_file: Path to PXF file
        project_name: Target project path
        balance_articles: Sync parts with database
        generate_auto_cables: Generate automatic cables
        verify: Run project check after import
    """
    return json.dumps(actions.import_pxf_project(
        import_file, project_name, balance_articles, generate_auto_cables, verify
    ), indent=2)


@mcp.tool()
def eplan_import_dwg_page(
    import_file: str,
    page_name: str,
    project_name: str = None,
    import_scheme: str = None,
    x_scale: float = 1.0,
    y_scale: float = 1.0,
    x_offset: float = 0.0,
    y_offset: float = 0.0
) -> str:
    """Insert DWG drawing into a page."""
    return json.dumps(actions.import_dwg_page(
        import_file, page_name, project_name, import_scheme,
        x_scale, y_scale, x_offset, y_offset
    ), indent=2)


@mcp.tool()
def eplan_import_dxf_page(
    import_file: str,
    page_name: str,
    project_name: str = None,
    import_scheme: str = None,
    x_scale: float = 1.0,
    y_scale: float = 1.0,
    x_offset: float = 0.0,
    y_offset: float = 0.0
) -> str:
    """Insert DXF drawing into a page."""
    return json.dumps(actions.import_dxf_page(
        import_file, page_name, project_name, import_scheme,
        x_scale, y_scale, x_offset, y_offset
    ), indent=2)


@mcp.tool()
def eplan_import_3d(
    import_file: str,
    project_name: str = None,
    import_scheme: str = None
) -> str:
    """Import 3D data."""
    return json.dumps(actions.import_3d(import_file, project_name, import_scheme), indent=2)


# ============================================================================
# PRINT
# ============================================================================

@mcp.tool()
def eplan_print_project(
    project_name: str = None,
    printer_name: str = None,
    copies: int = 1,
    collate: bool = True,
    reverse: bool = False,
    destination_file: str = None
) -> str:
    """Print a project."""
    return json.dumps(actions.print_project(
        project_name, printer_name, copies, collate, reverse, destination_file
    ), indent=2)


@mcp.tool()
def eplan_print_pages(
    page_name: str = None,
    project_name: str = None,
    printer_name: str = None,
    copies: int = 1,
    use_page_filter: bool = False,
    print_changed_only: bool = False
) -> str:
    """Print specific pages."""
    return json.dumps(actions.print_pages(
        page_name, project_name, printer_name, copies, use_page_filter, print_changed_only
    ), indent=2)


# ============================================================================
# CHECK / VERIFY
# ============================================================================

@mcp.tool()
def eplan_check_project(
    project_name: str = None,
    verification_scheme: str = None,
    verify_completed_only: bool = False
) -> str:
    """Check/verify a project for errors and warnings."""
    return json.dumps(actions.check_project(
        project_name, verification_scheme, verify_completed_only
    ), indent=2)


@mcp.tool()
def eplan_check_pages(
    page_name: str = None,
    project_name: str = None,
    verification_scheme: str = None,
    use_page_filter: bool = False
) -> str:
    """Check specific pages for errors and warnings."""
    return json.dumps(actions.check_pages(
        page_name, project_name, verification_scheme, use_page_filter
    ), indent=2)


@mcp.tool()
def eplan_check_parts(
    verification_scheme: str = None,
    verify_completed_only: bool = False
) -> str:
    """Check parts in the database."""
    return json.dumps(actions.check_parts(verification_scheme, verify_completed_only), indent=2)


# ============================================================================
# GENERATE
# ============================================================================

@mcp.tool()
def eplan_generate_connections(
    project_name: str = None,
    page_name: str = None,
    rebuild_all: bool = False,
    use_page_filter: bool = False
) -> str:
    """Generate connections in project."""
    return json.dumps(actions.generate_connections(
        project_name, page_name, rebuild_all, use_page_filter
    ), indent=2)


@mcp.tool()
def eplan_generate_cables(
    project_name: str = None,
    creation_scheme: str = None,
    numbering_scheme: str = None,
    autoselect_scheme: str = None,
    keep_old_names: bool = True,
    start_value: int = 1,
    step_value: int = 1,
    only_auto_cables: bool = True
) -> str:
    """Generate cables in project."""
    return json.dumps(actions.generate_cables(
        project_name, creation_scheme, numbering_scheme, autoselect_scheme,
        keep_old_names, start_value, step_value, only_auto_cables
    ), indent=2)


# ============================================================================
# REPORTS
# ============================================================================

@mcp.tool()
def eplan_update_reports(
    project_name: str = None,
    page_name: str = None,
    use_page_filter: bool = False
) -> str:
    """Update project reports/evaluations."""
    return json.dumps(actions.update_reports(project_name, page_name, use_page_filter), indent=2)


@mcp.tool()
def eplan_create_model_views(
    project_name: str = None,
    templates: List[str] = None,
    replace_existing: bool = False
) -> str:
    """Create model views."""
    return json.dumps(actions.create_model_views(project_name, templates, replace_existing), indent=2)


# ============================================================================
# SEARCH
# ============================================================================

@mcp.tool()
def eplan_search_devices(
    search_item: str,
    project_name: str = None,
    case_sensitive: bool = False,
    whole_text: bool = False
) -> str:
    """Search for devices in project."""
    return json.dumps(actions.search_devices(search_item, project_name, case_sensitive, whole_text), indent=2)


@mcp.tool()
def eplan_search_text(
    search_item: str,
    project_name: str = None,
    case_sensitive: bool = False,
    whole_text: bool = False,
    logic_pages: bool = True,
    graphic_pages: bool = True,
    evaluation_pages: bool = True
) -> str:
    """Search for text in project."""
    return json.dumps(actions.search_text(
        search_item, project_name, case_sensitive, whole_text,
        logic_pages, graphic_pages, evaluation_pages
    ), indent=2)


@mcp.tool()
def eplan_search_all_properties(
    search_item: str,
    project_name: str = None,
    case_sensitive: bool = False
) -> str:
    """Search through all properties in project."""
    return json.dumps(actions.search_all_properties(search_item, project_name, case_sensitive), indent=2)


# ============================================================================
# EDIT / NAVIGATION
# ============================================================================

@mcp.tool()
def eplan_open_page(
    page_name: str,
    project_name: str = None,
    x: float = None,
    y: float = None
) -> str:
    """Open a specific page in the editor."""
    return json.dumps(actions.edit_open_page(page_name, project_name, x, y), indent=2)


@mcp.tool()
def eplan_goto_device(device_name: str, project_name: str = None) -> str:
    """Navigate to a device in the project."""
    return json.dumps(actions.edit_goto_device(device_name, project_name), indent=2)


@mcp.tool()
def eplan_open_layout_space(installation_space: str, project_name: str = None) -> str:
    """Open a layout/installation space."""
    return json.dumps(actions.edit_open_layout_space(installation_space, project_name), indent=2)


@mcp.tool()
def eplan_close_pages() -> str:
    """Close all selected pages in the editor."""
    return json.dumps(actions.close_pages(), indent=2)


@mcp.tool()
def eplan_redraw() -> str:
    """Redraw the graphical editor."""
    return json.dumps(actions.redraw_ged(), indent=2)


# ============================================================================
# RENUMBER
# ============================================================================

@mcp.tool()
def eplan_renumber_devices(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    config_scheme: str = None,
    filter_scheme: str = None,
    identifier: str = None,
    use_selection: bool = False,
    post_numerate: bool = True,
    numerate_cables: bool = False
) -> str:
    """Renumber devices in project."""
    return json.dumps(actions.renumber_devices(
        project_name, start_value, step_value, config_scheme, filter_scheme,
        identifier, use_selection, post_numerate, numerate_cables
    ), indent=2)


@mcp.tool()
def eplan_renumber_pages(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    structure_oriented: bool = False,
    keep_interval: bool = False,
    keep_text: bool = False,
    use_selection: bool = False
) -> str:
    """Renumber pages in project."""
    return json.dumps(actions.renumber_pages(
        project_name, start_value, step_value, structure_oriented,
        keep_interval, keep_text, use_selection
    ), indent=2)


@mcp.tool()
def eplan_renumber_cables(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    config_scheme: str = None,
    use_selection: bool = False,
    keep_existing: bool = False,
    keep_identifier: bool = False
) -> str:
    """Renumber cables in project."""
    return json.dumps(actions.renumber_cables(
        project_name, start_value, step_value, config_scheme,
        use_selection, keep_existing, keep_identifier
    ), indent=2)


@mcp.tool()
def eplan_renumber_terminals(
    project_name: str = None,
    start_value: int = 1,
    step_value: int = 1,
    config_scheme: str = None,
    use_selection: bool = False,
    sequence: int = 0,
    prefix: str = None,
    suffix: str = None
) -> str:
    """
    Renumber terminals in project.

    Args:
        sequence: 0=Like sorting, 1=Page oriented, 2=Cable oriented, 3=Level oriented
    """
    return json.dumps(actions.renumber_terminals(
        project_name, start_value, step_value, config_scheme,
        use_selection, sequence, prefix, suffix
    ), indent=2)


# ============================================================================
# TRANSLATE
# ============================================================================

@mcp.tool()
def eplan_translate_project(project_name: str = None) -> str:
    """Translate a project using the translation database."""
    return json.dumps(actions.translate_project(project_name), indent=2)


@mcp.tool()
def eplan_export_missing_translations(
    export_file: str,
    language: str,
    project_name: str = None,
    converter: str = None
) -> str:
    """Export missing translations list."""
    return json.dumps(actions.export_missing_translations(
        export_file, language, project_name, converter
    ), indent=2)


@mcp.tool()
def eplan_remove_language(language: str, project_name: str = None) -> str:
    """Remove a language from project (e.g., "en_US" or "en_US,fr_FR")."""
    return json.dumps(actions.remove_language(language, project_name), indent=2)


# ============================================================================
# DEVICE LIST
# ============================================================================

@mcp.tool()
def eplan_export_device_list(
    export_file: str,
    project_name: str = None,
    format: str = "XDLXmlExporter"
) -> str:
    """Export device list from project."""
    return json.dumps(actions.export_device_list(export_file, project_name, format), indent=2)


@mcp.tool()
def eplan_import_device_list(
    import_file: str,
    project_name: str = None,
    format: str = "XDLXmlExporter"
) -> str:
    """Import device list into project."""
    return json.dumps(actions.import_device_list(import_file, project_name, format), indent=2)


@mcp.tool()
def eplan_delete_device_list(project_name: str = None) -> str:
    """Delete device list from project."""
    return json.dumps(actions.delete_device_list(project_name), indent=2)


# ============================================================================
# LABELING
# ============================================================================

@mcp.tool()
def eplan_create_labels(
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
) -> str:
    """Create labels for project (output: txt, xls, xlsx, xml)."""
    return json.dumps(actions.create_labels(
        destination_file, project_name, config_scheme, filter_scheme,
        sort_scheme, language, record_repeat, task_repeat, show_output, use_selection
    ), indent=2)


# ============================================================================
# PROJECT UTILITIES
# ============================================================================

@mcp.tool()
def eplan_compress_project(project_name: str = None) -> str:
    """Compress a project to reduce file size."""
    return json.dumps(actions.compress_project(project_name), indent=2)


@mcp.tool()
def eplan_synchronize_project(project_name: str = None) -> str:
    """Synchronize project data."""
    return json.dumps(actions.synchronize_project(project_name), indent=2)


# ============================================================================
# LAYER MANAGEMENT
# ============================================================================

@mcp.tool()
def eplan_change_layer(
    layer_name: str = None,
    visible: bool = None,
    printable: bool = None,
    editable: bool = None
) -> str:
    """Change graphical layer properties."""
    return json.dumps(actions.change_layer(layer_name, visible, printable, editable), indent=2)


@mcp.tool()
def eplan_export_layer_table(export_file: str, project_name: str = None) -> str:
    """Export graphical layer table."""
    return json.dumps(actions.export_graphical_layer_table(export_file, project_name), indent=2)


@mcp.tool()
def eplan_import_layer_table(import_file: str, project_name: str = None) -> str:
    """Import graphical layer table."""
    return json.dumps(actions.import_graphical_layer_table(import_file, project_name), indent=2)


# ============================================================================
# MACROS
# ============================================================================

@mcp.tool()
def eplan_generate_macros(
    project_name: str = None,
    destination_path: str = None,
    scheme: str = None
) -> str:
    """Generate macros from project."""
    return json.dumps(actions.generate_macros(project_name, destination_path, scheme), indent=2)


@mcp.tool()
def eplan_prepare_macros(project_name: str = None) -> str:
    """Prepare project for macro generation."""
    return json.dumps(actions.prepare_macros(project_name), indent=2)


@mcp.tool()
def eplan_update_macros(project_path: str = None) -> str:
    """Update macros in project."""
    return json.dumps(actions.update_macros(project_path), indent=2)


# ============================================================================
# SCRIPTS
# ============================================================================

@mcp.tool()
def eplan_register_script(script_file: str) -> str:
    """Register a script in EPLAN."""
    return json.dumps(actions.register_script(script_file), indent=2)


@mcp.tool()
def eplan_unregister_script(script_file: str) -> str:
    """Unregister a script from EPLAN."""
    return json.dumps(actions.unregister_script(script_file), indent=2)


@mcp.tool()
def eplan_execute_script(script_file: str) -> str:
    """Execute a registered script."""
    return json.dumps(actions.execute_script(script_file), indent=2)


# ============================================================================
# SETTINGS
# ============================================================================

@mcp.tool()
def eplan_export_settings(export_file: str, setting_type: str = None) -> str:
    """Export settings to XML file."""
    return json.dumps(actions.export_settings(export_file, setting_type), indent=2)


@mcp.tool()
def eplan_import_settings(import_file: str, setting_type: str = None) -> str:
    """Import settings from XML file."""
    return json.dumps(actions.import_settings(import_file, setting_type), indent=2)


@mcp.tool()
def eplan_set_setting(name: str, value: str) -> str:
    """Set a setting value."""
    return json.dumps(actions.set_setting(name, value), indent=2)


@mcp.tool()
def eplan_set_project_setting(name: str, value: str, project_name: str = None) -> str:
    """Set a project setting value."""
    return json.dumps(actions.set_project_setting(name, value, project_name), indent=2)


# ============================================================================
# PROPERTIES
# ============================================================================

@mcp.tool()
def eplan_get_project_property(property_id: str, project_name: str = None) -> str:
    """Get a property value from the project."""
    return json.dumps(actions.get_project_property(property_id, project_name), indent=2)


@mcp.tool()
def eplan_set_project_property(property_id: str, value: str, project_name: str = None) -> str:
    """Set a property value on the project."""
    return json.dumps(actions.set_project_property(property_id, value, project_name), indent=2)


@mcp.tool()
def eplan_get_page_property(property_id: str, page_name: str = None) -> str:
    """Get a property value from the first selected page."""
    return json.dumps(actions.get_page_property(property_id, page_name), indent=2)


@mcp.tool()
def eplan_set_page_property(property_id: str, value: str, page_name: str = None) -> str:
    """Set a property value on selected pages."""
    return json.dumps(actions.set_page_property(property_id, value, page_name), indent=2)


@mcp.tool()
def eplan_export_user_properties(export_file: str, project_name: str = None) -> str:
    """Export user properties to file."""
    return json.dumps(actions.export_user_properties(export_file, project_name), indent=2)


@mcp.tool()
def eplan_import_user_properties(import_file: str, project_name: str = None) -> str:
    """Import user properties from file."""
    return json.dumps(actions.import_user_properties(import_file, project_name), indent=2)


# ============================================================================
# PARTS MANAGEMENT
# ============================================================================

@mcp.tool()
def eplan_export_parts_list(export_file: str, project_name: str = None, format: str = None) -> str:
    """Export parts list from project."""
    return json.dumps(actions.export_parts_list(export_file, project_name, format), indent=2)


@mcp.tool()
def eplan_import_parts_list(import_file: str, project_name: str = None, format: str = None) -> str:
    """Import parts list into project."""
    return json.dumps(actions.import_parts_list(import_file, project_name, format), indent=2)


@mcp.tool()
def eplan_select_part() -> str:
    """Start the part selection dialog."""
    return json.dumps(actions.select_part(), indent=2)


@mcp.tool()
def eplan_set_parts_data_source(data_source: str) -> str:
    """Change the parts management database type."""
    return json.dumps(actions.set_parts_data_source(data_source), indent=2)


# ============================================================================
# PLC
# ============================================================================

@mcp.tool()
def eplan_plc_export(export_file: str, project_name: str = None, converter: str = None) -> str:
    """Export PLC data."""
    return json.dumps(actions.plc_export(export_file, project_name, converter), indent=2)


@mcp.tool()
def eplan_plc_import(import_file: str, project_name: str = None, converter: str = None) -> str:
    """Import PLC data."""
    return json.dumps(actions.plc_import(import_file, project_name, converter), indent=2)


# ============================================================================
# WORKSPACE
# ============================================================================

@mcp.tool()
def eplan_open_workspace(workspace_path: str) -> str:
    """Open an existing workspace."""
    return json.dumps(actions.open_workspace(workspace_path), indent=2)


@mcp.tool()
def eplan_save_workspace(workspace_path: str) -> str:
    """Save the current workspace."""
    return json.dumps(actions.save_workspace(workspace_path), indent=2)


@mcp.tool()
def eplan_clean_workspace() -> str:
    """Clean the current workspace."""
    return json.dumps(actions.clean_workspace(), indent=2)


# ============================================================================
# DATA EXCHANGE
# ============================================================================

@mcp.tool()
def eplan_export_connections(export_file: str, project_name: str = None) -> str:
    """Export connections from project."""
    return json.dumps(actions.export_connections(export_file, project_name), indent=2)


@mcp.tool()
def eplan_export_functions(export_file: str, project_name: str = None) -> str:
    """Export functions from project."""
    return json.dumps(actions.export_functions(export_file, project_name), indent=2)


@mcp.tool()
def eplan_export_pages(export_file: str, project_name: str = None) -> str:
    """Export pages from project."""
    return json.dumps(actions.export_pages(export_file, project_name), indent=2)


@mcp.tool()
def eplan_dc_import(import_file: str, project_name: str = None) -> str:
    """Import data configuration file into project."""
    return json.dumps(actions.dc_import(import_file, project_name), indent=2)


@mcp.tool()
def eplan_dc_export(export_file: str, project_name: str = None) -> str:
    """Export data configuration from project."""
    return json.dumps(actions.dc_export(export_file, project_name), indent=2)


# ============================================================================
# CONNECTIONS UTILITIES
# ============================================================================

@mcp.tool()
def eplan_correct_connections() -> str:
    """Merge graphical properties of connection definition points."""
    return json.dumps(actions.correct_connections(), indent=2)


@mcp.tool()
def eplan_remove_unnecessary_ndps() -> str:
    """Remove unnecessary net definition points."""
    return json.dumps(actions.remove_unnecessary_ndps(), indent=2)


@mcp.tool()
def eplan_unite_net_definition_points() -> str:
    """Unite net definition points on the same net."""
    return json.dumps(actions.unite_net_definition_points(), indent=2)


# ============================================================================
# SUBPROJECTS
# ============================================================================

@mcp.tool()
def eplan_export_subproject(export_file: str, project_name: str = None) -> str:
    """Export subproject."""
    return json.dumps(actions.export_subproject(export_file, project_name), indent=2)


@mcp.tool()
def eplan_import_subproject(import_file: str, project_name: str = None) -> str:
    """Import subproject."""
    return json.dumps(actions.import_subproject(import_file, project_name), indent=2)


# ============================================================================
# RIBBON BAR
# ============================================================================

@mcp.tool()
def eplan_export_ribbon_bar(export_file: str) -> str:
    """Export main ribbon bar customization to XML."""
    return json.dumps(actions.export_ribbon_bar(export_file), indent=2)


@mcp.tool()
def eplan_import_ribbon_bar(import_file: str) -> str:
    """Import main ribbon bar customization from XML."""
    return json.dumps(actions.import_ribbon_bar(import_file), indent=2)


# ============================================================================
# 3D / CABINET
# ============================================================================

@mcp.tool()
def eplan_calculate_cabinet_weight(project_name: str = None) -> str:
    """Calculate total weight of cabinet."""
    return json.dumps(actions.calculate_cabinet_weight(project_name), indent=2)


@mcp.tool()
def eplan_update_segments_filling(project_name: str = None) -> str:
    """Calculate and set segment filling values."""
    return json.dumps(actions.update_segments_filling(project_name), indent=2)


# ============================================================================
# PROJECT LANGUAGE
# ============================================================================

@mcp.tool()
def eplan_set_project_language(language: str, project_name: str = None, read_write: bool = True) -> str:
    """Set project language."""
    return json.dumps(actions.set_project_language(language, project_name, read_write), indent=2)


# ============================================================================
# PROJECT TYPE
# ============================================================================

@mcp.tool()
def eplan_switch_project_type(project_type: str, project_name: str = None) -> str:
    """Change the type of project."""
    return json.dumps(actions.switch_project_type(project_type, project_name), indent=2)


# ============================================================================
# SELECTION SET
# ============================================================================

@mcp.tool()
def eplan_get_current_project() -> str:
    """Get the current project path."""
    return json.dumps(actions.get_current_project(), indent=2)


@mcp.tool()
def eplan_get_selected_pages() -> str:
    """Get selected pages."""
    return json.dumps(actions.get_selected_pages(), indent=2)


# ============================================================================
# PREVIEW
# ============================================================================

@mcp.tool()
def eplan_preview_page(page_name: str = None, project_name: str = None, open: bool = True) -> str:
    """Open or close page preview."""
    return json.dumps(actions.preview_page(page_name, project_name, open), indent=2)


# ============================================================================
# NAVIGATION
# ============================================================================

@mcp.tool()
def eplan_navigate_to_eec(object_id: str) -> str:
    """Navigate to object in EPLAN Engineering Configuration."""
    return json.dumps(actions.navigate_to_eec(object_id), indent=2)


# ============================================================================
# TOPOLOGY
# ============================================================================

@mcp.tool()
def eplan_topology_operation(operation_type: str, project_name: str = None) -> str:
    """Perform topology-related operations."""
    return json.dumps(actions.topology_operation(operation_type, project_name), indent=2)


# ============================================================================
# PRE-PLANNING
# ============================================================================

@mcp.tool()
def eplan_import_preplanning_data(import_file: str, project_name: str = None) -> str:
    """Import pre-planning data."""
    return json.dumps(actions.import_preplanning_data(import_file, project_name), indent=2)


# ============================================================================
# SEGMENTS
# ============================================================================

@mcp.tool()
def eplan_export_segments_template(export_file: str, project_name: str = None) -> str:
    """Export segment templates to file."""
    return json.dumps(actions.export_segments_template(export_file, project_name), indent=2)


@mcp.tool()
def eplan_import_segments_template(import_file: str, project_name: str = None) -> str:
    """Import segment templates from file."""
    return json.dumps(actions.import_segments_template(import_file, project_name), indent=2)


# ============================================================================
# NC DATA / PRODUCTION
# ============================================================================

@mcp.tool()
def eplan_export_nc_data(export_file: str, project_name: str = None) -> str:
    """Export NC data for machines."""
    return json.dumps(actions.export_nc_data(export_file, project_name), indent=2)


@mcp.tool()
def eplan_export_production_wiring(export_file: str, project_name: str = None) -> str:
    """Export production wiring data for machines."""
    return json.dumps(actions.export_production_wiring(export_file, project_name), indent=2)


# ============================================================================
# API MODULE / ADD-INS
# ============================================================================

@mcp.tool()
def eplan_load_api_module(module_path: str) -> str:
    """Load and register an API add-in."""
    return json.dumps(actions.load_api_module(module_path), indent=2)


@mcp.tool()
def eplan_register_addon(addon_path: str) -> str:
    """Register an add-on."""
    return json.dumps(actions.register_addon(addon_path), indent=2)


@mcp.tool()
def eplan_unregister_addon(addon_path: str) -> str:
    """Unregister an add-on."""
    return json.dumps(actions.unregister_addon(addon_path), indent=2)


# ============================================================================
# RAW ACTION EXECUTION
# ============================================================================

@mcp.tool()
def eplan_execute_action(action_string: str) -> str:
    """
    Execute a raw EPLAN action string.
    Use this for actions not covered by specific functions.

    Args:
        action_string: Complete action string (e.g., "ActionName /PARAM1:value1")

    Example:
        eplan_execute_action('ProjectOpen /Project:"C:\\Projects\\test.elk"')
    """
    return json.dumps(actions.execute_raw_action(action_string), indent=2)


# ============================================================================
# TEST
# ============================================================================

@mcp.tool()
def eplan_test() -> str:
    """
    Show a MessageBox in EPLAN to verify the connection is working.
    Creates and executes a temporary C# script.
    """
    manager = get_manager(TARGET_VERSION)

    if not manager.connected:
        return json.dumps({
            "success": False,
            "message": "Not connected. Call eplan_connect() first."
        }, indent=2)

    # Create test script
    scripts_dir = os.path.join(SCRIPT_DIR, "scripts")
    os.makedirs(scripts_dir, exist_ok=True)
    script_path = os.path.join(scripts_dir, "mcp_test.cs")

    script = '''using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class MCPTest
{
    [Start]
    public void Run()
    {
        MessageBox.Show(
            "MCP Connection OK!",
            "EPLAN MCP Server",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information
        );
    }
}
'''
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script)

    # Register and execute
    manager.execute_action(f'RegisterScript /ScriptFile:"{script_path}"')
    result = manager.execute_action(f'ExecuteScript /ScriptFile:"{script_path}"')

    return json.dumps({
        "success": result.get("success", False),
        "message": "Check EPLAN for MessageBox" if result.get("success") else result.get("message")
    }, indent=2)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("EPLAN MCP Server")
    print(f"Target: EPLAN {TARGET_VERSION}")
    print("-" * 40)
    print("Available tool categories:")
    print("  - Connection: status, connect, disconnect, ping, test")
    print("  - Project: open, close, management, backup, restore")
    print("  - Export: PDF, DXF, DWG, graphics, PXF, 3D")
    print("  - Import: PXF, DXF/DWG, 3D")
    print("  - Print: project, pages")
    print("  - Check: project, pages, parts")
    print("  - Generate: connections, cables")
    print("  - Reports: update, create model views")
    print("  - Search: devices, text, properties")
    print("  - Edit: open page, goto device, layout space")
    print("  - Renumber: devices, pages, cables, terminals")
    print("  - Translate: project, export missing, remove language")
    print("  - Device list: export, import, delete")
    print("  - Labeling: create labels")
    print("  - Settings: export, import, set")
    print("  - Properties: get/set project, page, user")
    print("  - Parts: export, import, select, data source")
    print("  - PLC: export, import")
    print("  - Workspace: open, save, clean")
    print("  - Data exchange: connections, functions, pages")
    print("  - And more...")
    print("-" * 40)
    mcp.run()
