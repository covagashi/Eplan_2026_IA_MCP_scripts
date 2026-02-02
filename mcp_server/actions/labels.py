"""
Labeling actions.
"""

from ._base import _get_connected_manager, _build_action


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
