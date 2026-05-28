"""
API modules and add-on actions.
"""

from ._base import _get_connected_manager, _build_action


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
