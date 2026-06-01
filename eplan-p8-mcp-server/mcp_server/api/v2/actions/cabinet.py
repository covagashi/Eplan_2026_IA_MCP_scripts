"""
3D / Cabinet actions.
"""

from ._base import _get_connected_manager, _build_action


def calculate_cabinet_weight(project_name: str = None) -> dict:
    """
    Calculate total weight of cabinet.
    Action: XCabCalculateEnclosureTotalWeightAction
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "XCabCalculateEnclosureTotalWeightAction",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def update_segments_filling(project_name: str = None) -> dict:
    """
    Calculate and set segment filling values.
    Action: UpdateSegmentsFilling
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "UpdateSegmentsFilling",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def topology_operation(
    operation_type: str,
    project_name: str = None
) -> dict:
    """
    Perform topology-related operations.
    Action: Topology
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "Topology",
        TYPE=operation_type,
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def import_preplanning_data(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import pre-planning data.
    Action: ImportPrePlanningData
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ImportPrePlanningData",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)


def export_segments_template(
    export_file: str,
    project_name: str = None
) -> dict:
    """
    Export segment templates to file.
    Action: ExportSegmentsTemplate
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ExportSegmentsTemplate",
        PROJECTNAME=project_name,
        EXPORTFILE=export_file
    )
    return manager.execute_action(action)


def import_segments_template(
    import_file: str,
    project_name: str = None
) -> dict:
    """
    Import segment templates from file.
    Action: ImportSegmentsTemplate
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "ImportSegmentsTemplate",
        PROJECTNAME=project_name,
        IMPORTFILE=import_file
    )
    return manager.execute_action(action)
