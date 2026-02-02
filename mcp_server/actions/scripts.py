"""
Script registration and execution actions.
"""

from ._base import _get_connected_manager, _build_action


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
