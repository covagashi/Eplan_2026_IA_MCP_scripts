"""
EPLAN Actions Package

This package provides all EPLAN API actions organized by category.
All functions are re-exported here for backward compatibility.

Usage:
    from actions import open_project, export_pdf_project
    # or
    import actions
    actions.open_project(...)
"""

# Project management
from .project import (
    open_project,
    close_project,
    project_management,
    upgrade_projects,
    compress_project,
    synchronize_project,
    get_current_project,
    set_project_language,
    switch_project_type,
)

# Backup & restore
from .backup import (
    backup_project,
    backup_masterdata,
    restore_project,
    restore_masterdata,
)

# Export
from .export_ import (
    export_pdf_project,
    export_pdf_pages,
    export_dxf_project,
    export_dxf_pages,
    export_dwg_project,
    export_dwg_pages,
    export_dxfdwg_project_scheme,
    export_dxfdwg_pages_scheme,
    export_graphics_project,
    export_graphics_pages,
    export_pxf_project,
    export_3d,
)

# Import
from .import_ import (
    import_pxf_project,
    import_dwg_page,
    import_dxf_page,
    import_dxfdwg_files,
    import_pdf_comments,
    import_3d,
)

# Print
from .print_ import (
    print_project,
    print_pages,
)

# Verify/Check
from .verify import (
    check_project,
    check_pages,
    check_parts,
)

# Generate
from .generate import (
    generate_connections,
    generate_cables,
)

# Reports
from .reports import (
    update_reports,
    update_model_view_pages,
    create_model_views,
    create_copper_unfolds,
    create_drilling_views,
)

# Search
from .search import (
    search_devices,
    search_text,
    search_all_properties,
    search_page_data,
    search_project_data,
)

# Navigation / Edit
from .navigation import (
    edit_open_page,
    edit_goto_device,
    edit_open_layout_space,
    close_pages,
    redraw_ged,
    get_selected_pages,
    preview_page,
    navigate_to_eec,
)

# Renumber
from .renumber import (
    renumber_devices,
    renumber_pages,
    renumber_cables,
    renumber_terminals,
    renumber_connections,
)

# Translate
from .translate import (
    translate_project,
    export_missing_translations,
    remove_language,
)

# Device list
from .devicelist import (
    export_device_list,
    import_device_list,
    delete_device_list,
)

# Labels
from .labels import (
    create_labels,
)

# Layers
from .layers import (
    change_layer,
    export_graphical_layer_table,
    import_graphical_layer_table,
)

# Macros
from .macros import (
    generate_macros,
    prepare_macros,
    update_macros,
)

# Scripts
from .scripts import (
    register_script,
    unregister_script,
    execute_script,
)

# Settings
from .settings import (
    export_settings,
    import_settings,
    set_setting,
    set_project_setting,
)

# Properties
from .properties import (
    get_project_property,
    set_project_property,
    get_page_property,
    set_page_property,
    get_property,
    set_property,
    export_user_properties,
    import_user_properties,
)

# Parts management
from .parts import (
    export_parts_list,
    import_parts_list,
    select_part,
    set_parts_data_source,
)

# Parts management API
from .partsmanagement import (
    partsmanagement_export,
    partsmanagement_import,
    partsmanagement_export_by_properties,
    partsmanagement_export_all,
)

# PLC
from .plc import (
    plc_export,
    plc_import,
)

# Workspace
from .workspace import (
    open_workspace,
    save_workspace,
    clean_workspace,
)

# Data exchange
from .data_exchange import (
    export_connections,
    export_functions,
    export_pages,
    dc_import,
    dc_export,
    export_dc_article_data,
    import_dc_article_data,
    export_location_boxes,
    export_potential_definitions,
    export_pipeline_definitions,
    delete_representation_type,
    correct_connections,
    remove_unnecessary_ndps,
    unite_net_definition_points,
    export_subproject,
    import_subproject,
    masterdata_operation,
)

# Cabinet / 3D
from .cabinet import (
    calculate_cabinet_weight,
    update_segments_filling,
    topology_operation,
    import_preplanning_data,
    export_segments_template,
    import_segments_template,
)

# Production
from .production import (
    export_nc_data,
    export_production_wiring,
)

# Ribbon bar
from .ribbon import (
    export_ribbon_bar,
    import_ribbon_bar,
)

# Add-ons and raw execution
from .addons import (
    load_api_module,
    register_addon,
    unregister_addon,
    execute_raw_action,
)

# Scripted actions (C# scripts for advanced APIs)
from .scripted import (
    # Parts database (MDPartsManagement)
    parts_db_query,
    parts_db_count,
    parts_db_get_part,
    parts_db_update,
    parts_db_list_product_groups,
    # Settings API (typed)
    settings_get_string,
    settings_set_string,
    settings_get_bool,
    settings_set_bool,
    settings_get_int,
    settings_set_int,
    settings_get_double,
    settings_set_double,
    # PathMap
    pathmap_substitute,
    pathmap_get_common_paths,
    # Custom scripts
    execute_custom_script,
)

# Re-export base utilities for advanced usage
from ._base import (
    _get_connected_manager,
    _build_action,
    TARGET_VERSION,
)


__all__ = [
    # Project
    'open_project', 'close_project', 'project_management', 'upgrade_projects',
    'compress_project', 'synchronize_project', 'get_current_project',
    'set_project_language', 'switch_project_type',
    # Backup
    'backup_project', 'backup_masterdata', 'restore_project', 'restore_masterdata',
    # Export
    'export_pdf_project', 'export_pdf_pages', 'export_dxf_project', 'export_dxf_pages',
    'export_dwg_project', 'export_dwg_pages', 'export_dxfdwg_project_scheme',
    'export_dxfdwg_pages_scheme', 'export_graphics_project', 'export_graphics_pages',
    'export_pxf_project', 'export_3d',
    # Import
    'import_pxf_project', 'import_dwg_page', 'import_dxf_page', 'import_dxfdwg_files',
    'import_pdf_comments', 'import_3d',
    # Print
    'print_project', 'print_pages',
    # Verify
    'check_project', 'check_pages', 'check_parts',
    # Generate
    'generate_connections', 'generate_cables',
    # Reports
    'update_reports', 'update_model_view_pages', 'create_model_views',
    'create_copper_unfolds', 'create_drilling_views',
    # Search
    'search_devices', 'search_text', 'search_all_properties',
    'search_page_data', 'search_project_data',
    # Navigation
    'edit_open_page', 'edit_goto_device', 'edit_open_layout_space',
    'close_pages', 'redraw_ged', 'get_selected_pages', 'preview_page', 'navigate_to_eec',
    # Renumber
    'renumber_devices', 'renumber_pages', 'renumber_cables', 'renumber_terminals',
    'renumber_connections',
    # Translate
    'translate_project', 'export_missing_translations', 'remove_language',
    # Device list
    'export_device_list', 'import_device_list', 'delete_device_list',
    # Labels
    'create_labels',
    # Layers
    'change_layer', 'export_graphical_layer_table', 'import_graphical_layer_table',
    # Macros
    'generate_macros', 'prepare_macros', 'update_macros',
    # Scripts
    'register_script', 'unregister_script', 'execute_script',
    # Settings
    'export_settings', 'import_settings', 'set_setting', 'set_project_setting',
    # Properties
    'get_project_property', 'set_project_property', 'get_page_property',
    'set_page_property', 'get_property', 'set_property',
    'export_user_properties', 'import_user_properties',
    # Parts
    'export_parts_list', 'import_parts_list', 'select_part', 'set_parts_data_source',
    # Parts management API
    'partsmanagement_export', 'partsmanagement_import',
    'partsmanagement_export_by_properties', 'partsmanagement_export_all',
    # PLC
    'plc_export', 'plc_import',
    # Workspace
    'open_workspace', 'save_workspace', 'clean_workspace',
    # Data exchange
    'export_connections', 'export_functions', 'export_pages',
    'dc_import', 'dc_export', 'export_dc_article_data', 'import_dc_article_data',
    'export_location_boxes', 'export_potential_definitions', 'export_pipeline_definitions',
    'delete_representation_type', 'correct_connections', 'remove_unnecessary_ndps',
    'unite_net_definition_points', 'export_subproject', 'import_subproject',
    'masterdata_operation',
    # Cabinet
    'calculate_cabinet_weight', 'update_segments_filling', 'topology_operation',
    'import_preplanning_data', 'export_segments_template', 'import_segments_template',
    # Production
    'export_nc_data', 'export_production_wiring',
    # Ribbon
    'export_ribbon_bar', 'import_ribbon_bar',
    # Add-ons
    'load_api_module', 'register_addon', 'unregister_addon', 'execute_raw_action',
    # Scripted - Parts database
    'parts_db_query', 'parts_db_count', 'parts_db_get_part', 'parts_db_update',
    'parts_db_list_product_groups',
    # Scripted - Settings API
    'settings_get_string', 'settings_set_string', 'settings_get_bool', 'settings_set_bool',
    'settings_get_int', 'settings_set_int', 'settings_get_double', 'settings_set_double',
    # Scripted - PathMap
    'pathmap_substitute', 'pathmap_get_common_paths',
    # Scripted - Custom
    'execute_custom_script',
    # Base
    '_get_connected_manager', '_build_action', 'TARGET_VERSION',
]
