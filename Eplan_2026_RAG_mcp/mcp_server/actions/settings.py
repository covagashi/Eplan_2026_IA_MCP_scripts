"""
Settings and configuration actions.
"""

from ._base import _get_connected_manager, _build_action


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
