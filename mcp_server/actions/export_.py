"""
Export actions (PDF, DXF, DWG, graphics, PXF, 3D, etc.)
Complete implementation with all documented parameters.
"""

from typing import List, Optional
from ._base import _get_connected_manager, _build_action


def export_pdf_project(
    export_file: str,
    project_name: str = None,
    export_scheme: str = None,
    black_white: int = 0,
    language: str = None,
    use_zoom: bool = False,
    zoom_level: int = None,
    use_simple_link: bool = False,
    fast_web_view: bool = False,
    read_only: bool = False,
    use_print_margins: bool = None,
    export_model: bool = False
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
        use_simple_link: Only create simple links in PDF (no three-way jumps)
        fast_web_view: Enable fast web display
        read_only: Make PDF write-protected
        use_print_margins: Use print margins (None=from scheme)
        export_model: Export 3D models along with pages
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    params = {
        "TYPE": "PDFPROJECTSCHEME",
        "PROJECTNAME": project_name,
        "EXPORTFILE": export_file,
        "EXPORTSCHEME": export_scheme,
        "BLACKWHITE": black_white,
        "LANGUAGE": language,
        "USEZOOM": use_zoom,
        "ZOOMLEVEL": zoom_level,
        "USESIMPLELINK": use_simple_link,
        "FASTWEBVIEW": fast_web_view,
        "READONLYEXPORT": read_only,
        "EXPORTMODEL": export_model,
    }

    if use_print_margins is not None:
        params["USEPRINTMARGINS"] = use_print_margins

    action = _build_action("export", **params)
    return manager.execute_action(action)


def export_pdf_pages(
    export_file: str,
    page_names: List[str] = None,
    page_identifiers: List[str] = None,
    project_name: str = None,
    export_scheme: str = None,
    black_white: int = 0,
    language: str = None,
    use_zoom: bool = False,
    zoom_level: int = None,
    use_simple_link: bool = False,
    fast_web_view: bool = False,
    read_only: bool = False,
    use_print_margins: bool = None,
    export_model: bool = False
) -> dict:
    """
    Export specific pages to PDF format.
    Action: export

    Args:
        export_file: Output PDF file path
        page_names: List of page names (e.g., ["=AP+ST1/2", "=AP+ST1/4"])
        page_identifiers: List of page identifiers from StorableObject.ToStringIdentifier()
        project_name: Project path (optional)
        export_scheme: PDF export scheme name
        black_white: 0=Color, 1=B&W, 2=Grayscale, 3=White Inverted
        language: Language code
        use_zoom: Enable zoom window
        zoom_level: Zoom level in mm (1-3500)
        use_simple_link: Only simple links
        fast_web_view: Enable fast web display
        read_only: Write-protected PDF
        use_print_margins: Use print margins
        export_model: Export 3D models
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    parts = ["export", "/TYPE:PDFPAGESSCHEME", f'/EXPORTFILE:"{export_file}"']

    if project_name:
        parts.append(f'/PROJECTNAME:"{project_name}"')
    if export_scheme:
        parts.append(f'/EXPORTSCHEME:"{export_scheme}"')

    parts.append(f"/BLACKWHITE:{black_white}")

    if language:
        parts.append(f"/LANGUAGE:{language}")
    if use_zoom:
        parts.append("/USEZOOM:1")
    if zoom_level:
        parts.append(f"/ZOOMLEVEL:{zoom_level}")
    if use_simple_link:
        parts.append("/USESIMPLELINK:1")
    if fast_web_view:
        parts.append("/FASTWEBVIEW:1")
    if read_only:
        parts.append("/READONLYEXPORT:1")
    if use_print_margins is not None:
        parts.append(f"/USEPRINTMARGINS:{1 if use_print_margins else 0}")
    if export_model:
        parts.append("/EXPORTMODEL:1")

    # Add page names
    if page_names:
        for i, page in enumerate(page_names, 1):
            parts.append(f'/PAGENAME{i}:"{page}"')

    # Add page identifiers (SELn)
    if page_identifiers:
        for i, sel in enumerate(page_identifiers, 1):
            parts.append(f"/SEL{i}:{sel}")

    return manager.execute_action(" ".join(parts))


def export_dxf_project(
    destination_path: str,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None,
    target: str = None
) -> dict:
    """
    Export project to DXF format.
    Action: export

    Args:
        destination_path: Output directory
        project_name: Project path (optional)
        export_scheme: DXF export scheme
        language: Language code (case-sensitive, e.g., "en_US")
        target: "Disk" or "FromSettings"
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
        LANGUAGE=language,
        TARGET=target
    )
    return manager.execute_action(action)


def export_dxf_pages(
    destination_path: str = None,
    page_name: str = None,
    page_names: List[str] = None,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None,
    target: str = None
) -> dict:
    """
    Export pages to DXF format.
    Action: export

    Args:
        destination_path: Output directory (ignored if using PAGENAMEn with scheme)
        page_name: Single page name
        page_names: List of page names for multiple export
        project_name: Project path (optional)
        export_scheme: DXF export scheme
        language: Language code
        target: "Disk" or "FromSettings"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    parts = ["export", "/TYPE:DXFPAGE"]

    if project_name:
        parts.append(f'/PROJECTNAME:"{project_name}"')
    if destination_path:
        parts.append(f'/DESTINATIONPATH:"{destination_path}"')
    if export_scheme:
        parts.append(f'/EXPORTSCHEME:"{export_scheme}"')
    if language:
        parts.append(f"/LANGUAGE:{language}")
    if target:
        parts.append(f"/TARGET:{target}")

    if page_name:
        parts.append(f'/PAGENAME:"{page_name}"')

    if page_names:
        for i, page in enumerate(page_names, 1):
            parts.append(f'/PAGENAME{i}:"{page}"')

    return manager.execute_action(" ".join(parts))


def export_dwg_project(
    destination_path: str,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None,
    target: str = None
) -> dict:
    """
    Export project to DWG format.
    Action: export

    Args:
        destination_path: Output directory
        project_name: Project path (optional)
        export_scheme: DWG export scheme
        language: Language code
        target: "Disk" or "FromSettings"
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
        LANGUAGE=language,
        TARGET=target
    )
    return manager.execute_action(action)


def export_dwg_pages(
    destination_path: str = None,
    page_name: str = None,
    page_names: List[str] = None,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None,
    target: str = None
) -> dict:
    """
    Export pages to DWG format.
    Action: export

    Args:
        destination_path: Output directory
        page_name: Single page name
        page_names: List of page names
        project_name: Project path (optional)
        export_scheme: DWG export scheme
        language: Language code
        target: "Disk" or "FromSettings"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    parts = ["export", "/TYPE:DWGPAGE"]

    if project_name:
        parts.append(f'/PROJECTNAME:"{project_name}"')
    if destination_path:
        parts.append(f'/DESTINATIONPATH:"{destination_path}"')
    if export_scheme:
        parts.append(f'/EXPORTSCHEME:"{export_scheme}"')
    if language:
        parts.append(f"/LANGUAGE:{language}")
    if target:
        parts.append(f"/TARGET:{target}")

    if page_name:
        parts.append(f'/PAGENAME:"{page_name}"')

    if page_names:
        for i, page in enumerate(page_names, 1):
            parts.append(f'/PAGENAME{i}:"{page}"')

    return manager.execute_action(" ".join(parts))


def export_dxfdwg_project_scheme(
    project_name: str = None,
    export_scheme: str = None,
    language: str = None,
    target: str = "FromSettings"
) -> dict:
    """
    Export project to DXF or DWG format using scheme settings.
    Format (DXF or DWG) is determined by the scheme.
    Action: export

    Args:
        project_name: Project path (optional)
        export_scheme: Export scheme (determines DXF or DWG)
        language: Language code
        target: "Disk" or "FromSettings" (default)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export",
        TYPE="DXFDWGPROJECTSCHEME",
        PROJECTNAME=project_name,
        EXPORTSCHEME=export_scheme,
        LANGUAGE=language,
        TARGET=target
    )
    return manager.execute_action(action)


def export_dxfdwg_pages_scheme(
    page_names: List[str] = None,
    page_identifiers: List[str] = None,
    project_name: str = None,
    export_scheme: str = None,
    language: str = None,
    target: str = "FromSettings"
) -> dict:
    """
    Export pages to DXF or DWG format using scheme settings.
    Format is determined by the scheme.
    Action: export

    Args:
        page_names: List of page names
        page_identifiers: List of page identifiers (SELn)
        project_name: Project path (optional)
        export_scheme: Export scheme
        language: Language code
        target: "Disk" or "FromSettings"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    parts = ["export", "/TYPE:DXFDWGPPAGESSCHEME"]

    if project_name:
        parts.append(f'/PROJECTNAME:"{project_name}"')
    if export_scheme:
        parts.append(f'/EXPORTSCHEME:"{export_scheme}"')
    if language:
        parts.append(f"/LANGUAGE:{language}")
    if target:
        parts.append(f"/TARGET:{target}")

    if page_names:
        for i, page in enumerate(page_names, 1):
            parts.append(f'/PAGENAME{i}:"{page}"')

    if page_identifiers:
        for i, sel in enumerate(page_identifiers, 1):
            parts.append(f"/SEL{i}:{sel}")

    return manager.execute_action(" ".join(parts))


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
        color_depth: 1, 4, 8, 16, 24, or 32
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


def export_graphics_pages(
    destination_path: str,
    page_name: str = None,
    project_name: str = None,
    format: str = "PNG",
    color_depth: int = 24,
    image_width: int = 1024,
    black_white: bool = False,
    compression: str = "NONE",
    use_page_filter: bool = False
) -> dict:
    """
    Export pages to graphical format (PNG, TIF, GIF, JPG, BMP).
    Action: export

    Args:
        destination_path: Output directory
        page_name: Specific page name (optional, if not set uses filter or all)
        project_name: Project path (optional)
        format: Image format - "PNG", "TIF", "GIF", "JPG", "BMP"
        color_depth: 1, 4, 8, 16, 24, or 32
        image_width: Image width in pixels
        black_white: Black and white output
        compression: For TIF - "LZW", "RLE", "CCITT3", "CCITT4", "NONE"
        use_page_filter: Use active page filter (ignored if page_name is set)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "export",
        TYPE="GRAPHICPAGE",
        PROJECTNAME=project_name,
        DESTINATIONPATH=destination_path,
        PAGENAME=page_name,
        FORMAT=format,
        COLORDEPTH=color_depth,
        IMAGEWIDTH=image_width,
        BLACKWHITE=black_white,
        IMAGECOMPRESSION=compression,
        USEPAGEFILTER=use_page_filter
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
        export_file: Output file path (extension added automatically)
        project_name: Project path (optional)
        export_masterdata: Include master data (default True)
        export_connections: Include connections (default False)
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
