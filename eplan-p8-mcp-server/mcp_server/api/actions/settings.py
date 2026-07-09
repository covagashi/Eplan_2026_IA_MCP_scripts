"""
Settings and configuration actions.
"""

from ._base import _get_connected_manager, _build_action


def export_settings(
    xml_file: str,
    node: str = None,
    project: str = None
) -> dict:
    """
    Export settings to an XML file.
    Action: XSettingsExport

    Args:
        xml_file: Full name of the target XML file (parameter XMLFile).
        node: Path of a setting node, e.g. "USER", "STATION", "COMPANY",
              "USER.DIALOGSETTINGS" (parameter node, without PROJECT).
        project: Project (must be open) for exporting project settings
                 (parameter prj).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsExport",
        XMLFile=xml_file,
        node=node,
        prj=project
    )
    return manager.execute_action(action)


def import_settings(
    xml_file: str,
    node: str = None,
    project: str = None
) -> dict:
    """
    Import project-, station-, company- or user settings from an XML file.
    Action: XSettingsImport

    Args:
        xml_file: Full name of the XML file (parameter XmlFile). If empty,
                  a file selection dialog appears.
        node: Node of settings to import (parameter Node), e.g.
              "User.XSbGui.CustomSymbols".
        project: Full name of the target project for project settings
                 (parameter Project).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsImport",
        XmlFile=xml_file,
        Node=node,
        Project=project
    )
    return manager.execute_action(action)


def set_setting(name: str, value: str, index: int = 0) -> dict:
    """
    Set the value of a setting.
    Action: XAfActionSetting

    Args:
        name: Name of the setting to set (parameter set),
              e.g. "USER.MacrosLog.Pxf.writeDebugInfo".
        value: New value of the setting (parameter value).
        index: Optional index of the setting (parameter index, default 0).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XAfActionSetting",
        set=name,
        value=value,
        index=index
    )
    return manager.execute_action(action)


def set_project_setting(name: str, value: str, project: str = None, index: int = 0) -> dict:
    """
    Set the value of a project setting.
    Action: XAfActionSettingProject

    Args:
        name: Name of the project setting to set (parameter set).
        value: New value of the setting (parameter value).
        project: Full name of the target project (parameter Project).
                 When empty, the currently selected project is used.
        index: Optional index of the setting (parameter index, default 0).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XAfActionSettingProject",
        Project=project,
        set=name,
        value=value,
        index=index
    )
    return manager.execute_action(action)
