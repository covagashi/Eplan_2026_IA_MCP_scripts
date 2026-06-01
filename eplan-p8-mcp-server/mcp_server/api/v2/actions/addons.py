"""
API modules and add-on actions.
"""

from ._base import _get_connected_manager, _build_action


def load_api_module(module_path: str) -> dict:
    """
    Load and register an API add-in.
    Action: EplApiModuleAction

    Args:
        module_path: File name of the Add-in DLL to register (parameter register).
                     If no absolute path is given, it is resolved against the
                     current directory.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "EplApiModuleAction",
        register=module_path
    )
    return manager.execute_action(action)


def register_addon(addon_path: str = None, install_file: str = None) -> dict:
    """
    Register an add-on.
    Action: XSettingsRegisterAction

    Args:
        addon_path: Path where the add-on is located, e.g. "..\\addon\\1.0.0"
                    (parameter path). Alternative to install_file.
        install_file: Complete path of the install.xml file (parameter installFile).
                      Alternative to addon_path.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsRegisterAction",
        path=addon_path,
        installFile=install_file
    )
    return manager.execute_action(action)


def unregister_addon(addon_path: str = None, install_file: str = None) -> dict:
    """
    Unregister an add-on.
    Action: XSettingsUnregisterAction

    Args:
        addon_path: Path where the add-on is located (parameter path).
                    Alternative to install_file.
        install_file: Complete path of the install.xml file (parameter installFile).
                      Alternative to addon_path.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XSettingsUnregisterAction",
        path=addon_path,
        installFile=install_file
    )
    return manager.execute_action(action)


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
