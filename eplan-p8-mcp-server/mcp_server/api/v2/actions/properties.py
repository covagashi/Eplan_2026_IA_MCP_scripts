"""
Property actions (project, page, user properties, and generic properties).
Complete implementation with all documented parameters.
"""

from typing import Optional
from ._base import _get_connected_manager, _build_action


def get_project_property(property_id: str, project_name: str = None) -> dict:
    """
    Get a property value from the project.
    Action: XEsGetProjectPropertyAction

    Args:
        property_id: Property identifier (number or name)
        project_name: Project path (optional)
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

    Args:
        property_id: Property identifier (number or name)
        value: Value to set
        project_name: Project path (optional)
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

    Args:
        property_id: Property identifier (number or name)
        page_name: Page name (optional, uses selected page if not set)
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

    Args:
        property_id: Property identifier (number or name)
        value: Value to set
        page_name: Page name (optional, uses selected pages if not set)
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


def get_property(
    property_id: str = None,
    property_ident_name: str = None,
    property_index: int = 0
) -> dict:
    """
    Get a property from selected objects.
    Action: XEsGetPropertyAction

    Args:
        property_id: Property identifier number (from Eplan.EplApi.DataModel.Properties)
        property_ident_name: Property identifier name (for user-defined properties)
        property_index: Property index (default 0)

    Note:
        Either property_id or property_ident_name must be provided.
        Returns the property value in the result.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    if property_id:
        action = _build_action(
            "XEsGetPropertyAction",
            PropertyId=property_id,
            PropertyIndex=property_index
        )
    elif property_ident_name:
        action = _build_action(
            "XEsGetPropertyAction",
            PropertyIdentName=property_ident_name,
            PropertyIndex=property_index
        )
    else:
        return {"success": False, "message": "Either property_id or property_ident_name must be provided"}

    return manager.execute_action(action)


def set_property(
    value: str,
    property_id: str = None,
    property_ident_name: str = None,
    property_index: int = 0
) -> dict:
    """
    Set a property on selected objects.
    Action: XEsSetPropertyAction

    Args:
        value: Value to set
        property_id: Property identifier number
        property_ident_name: Property identifier name (for user-defined properties)
        property_index: Property index (default 0)

    Note:
        Either property_id or property_ident_name must be provided.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    if property_id:
        action = _build_action(
            "XEsSetPropertyAction",
            PropertyId=property_id,
            PropertyIndex=property_index,
            PropertyValue=value
        )
    elif property_ident_name:
        action = _build_action(
            "XEsSetPropertyAction",
            PropertyIdentName=property_ident_name,
            PropertyIndex=property_index,
            PropertyValue=value
        )
    else:
        return {"success": False, "message": "Either property_id or property_ident_name must be provided"}

    return manager.execute_action(action)


def export_user_properties(export_file: str, project_name: str = None) -> dict:
    """
    Export user properties to file.
    Action: XEsUserPropertiesExportAction

    Args:
        export_file: Output file path
        project_name: Project path (optional)
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

    Args:
        import_file: Input file path
        project_name: Project path (optional)
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
