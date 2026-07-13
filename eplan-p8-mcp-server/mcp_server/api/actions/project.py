"""
Project management actions.
"""

from typing import List
from ._base import _get_connected_manager, _build_action


def open_project(project_path: str, open_mode: str = None) -> dict:
    """
    Open a project in EPLAN.
    Action: ProjectOpen

    IMPORTANT: Never guess, assume, or reuse a previously-seen project path.
    Always ask the user which project they want to open before calling this
    tool, unless they already gave you the exact path in this turn.

    Args:
        project_path: Full path to the project file (.elk)
        open_mode: Optional - "Standard", "ReadOnly", or "Exclusive"
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action("ProjectOpen", Project=project_path, OpenMode=open_mode)
    return manager.execute_action(action)


def close_project() -> dict:
    """
    Close the currently open project in EPLAN.
    Action: XPrjActionProjectClose

    IMPORTANT: This runs under QuietMode, which suppresses EPLAN's other
    dialogs (not necessarily an "unsaved changes" prompt specifically).
    Never assume it is safe to close - always ask the user to confirm before
    calling this tool, unless they already explicitly asked you to close the
    project in this turn.

    IMPORTANT - which project actually gets closed: XPrjActionProjectClose
    takes no project name/path argument. It closes whichever project
    currently has window focus in the EPLAN GUI (i.e. whichever one the user
    last clicked into), determined purely by mouse/window focus - not by
    anything this API can query or set. selectionset /TYPE:PROJECTS and
    /TYPE:PROJECT were both tested (2026-07-13) and always mirror the same
    single focused project; neither lists "all open projects", so there is
    no reliable way from here to confirm or choose which project will close
    when more than one is open. If it matters which project closes, ask the
    user to confirm which one currently has focus in EPLAN before calling
    this.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    return manager.execute_action("XPrjActionProjectClose")


def project_management(
    type: str,
    project_name: str = None,
    filename: str = None,
    scheme: str = None,
    overwrite: bool = None,
    extended_mode: bool = None,
    projects_directory: str = None,
    scan_subdirectories: bool = None
) -> dict:
    """
    Project management operations.
    Action: projectmanagement

    IMPORTANT: Always ask the user for the exact project_name (full path,
    e.g. "C:\\Projects\\EPLAN\\Sample.elk") before calling this - never guess
    or reuse a previously-seen path. Per the official docs, PROJECTNAME is
    only truly optional when this is invoked interactively from the EPLAN
    GUI with a project already selected there; called the way this MCP
    server calls it (command-line style), omitting it throws
    System.ArgumentException - and this wrapper swallows that exception
    silently, returning an unhelpful {"success": false} with no error text.

    IMPORTANT - success:true is not always proof something real happened.
    Confirmed twice (2026-07-13): READPROJECTINFO returned success:true even
    when fed an XML of the wrong schema (no visible effect, contents
    unverified), and CORRECTPROJECTITEMS returned success:true while leaving
    every file in the project database byte-for-byte, timestamp-for-timestamp
    unchanged. If it matters whether the action actually did something,
    verify independently (e.g. check file timestamps/sizes on disk) rather
    than trusting success:true alone.

    All 8 `type` values were tested end-to-end on 2026-07-13. What each one
    actually does, confirmed by observing real output on disk (not just
    guessed from the docstring):

    - "READPROJECTINFO": NOT read-only despite the name - it imports data
      FROM an XML file INTO the project (a write). Requires `filename`
      pointing at a real "ProjectInfo.xml"-schema file (one exists inside
      any project's own `<project>.edb/ProjectInfo.xml` - use that as a
      reference/source, not an arbitrary XML). Feeding it an XML of a
      different schema (e.g. a PropertyView export) still returns
      success:true - do not treat that as confirmation it worked.

    - "PUBLISHSMARTPRODUCTION": exports the project's EPLAN Smart Production
      manufacturing data. `filename` is a base path - EPLAN ignores whatever
      extension you give it and always appends its own; the real output is
      a `.epdz` file (a genuine 7-zip archive), e.g.
      filename="C:\\out\\myexport" -> creates "myexport.epdz". Read-only on
      the source project.

    - "CREATESNAPSHOTCOPY": creates a full copy of the project as a new,
      independent EPLAN project. `filename` is the target base path - like
      PUBLISHSMARTPRODUCTION, any extension you give is irrelevant and
      discarded; EPLAN always creates "<base>.elk" + "<base>.edb" (a real,
      openable project). Don't bother adding an extension - just pass the
      base path/name you want.

    - "EXPORTPROPERTYPLACEMENTSSCHEMAS": genuine read-only export - writes
      the project's property-placement schemes to a real XML file at
      `filename` (extension IS respected here, unlike the two above). This
      is the correct way to produce a schemes XML if the user doesn't
      already have one - it pairs with IMPORTPROPERTYPLACEMENTSSCHEMAS
      below (same schema, round-trip tested and confirmed). Do NOT use its
      output as input to READPROJECTINFO - different schema, silently
      "succeeds" without doing anything meaningful.

    - "IMPORTPROPERTYPLACEMENTSSCHEMAS": the counterpart to
      EXPORTPROPERTYPLACEMENTSSCHEMAS - imports a schemes XML (produced by
      the export above) into `project_name`. Set `overwrite=True` if the
      target project may already have a scheme of the same name. Confirmed
      working with a real export->import round trip across two projects.

    - "REORGANIZE": irreversible maintenance operation. Per official docs:
      "deleted data is irretrievably removed from the project database. The
      project database is reduced in size." Only purges data already marked
      deleted (doesn't touch active/live data), but that purge cannot be
      undone. Confirmed on disk: internal database files were rewritten and
      shrank measurably. Always confirm with the user before calling.

    - "CORRECTPROJECTITEMS": designed to automatically correct, synchronize,
      and repair inconsistent elements/data within a project. Takes
      `scheme` (e.g. "Default" per official docs example). Irreversible-ish
      modification, confirm with the user first. Confirmed success:true can
      happen with zero observable effect on disk - don't assume it changed
      anything without checking.

    - "LOADDIRECTORY": scans a directory for EPLAN projects and registers
      them in the GUI's Project Manager - does not modify the projects
      themselves, purely additive/discovery. Can run "stand-alone" (no
      params, scans the user's default projects path) or with
      `projects_directory` (+ `scan_subdirectories`). This wrapper does NOT
      return the list of projects found - confirmed the result only echoes
      back the input parameters. If the user needs to know what was found,
      either check the filesystem directly or ask the user to look at the
      EPLAN GUI themselves.

    Args:
        type: Task type - see the detailed behavior notes above for each of:
              "READPROJECTINFO", "PUBLISHSMARTPRODUCTION", "CREATESNAPSHOTCOPY",
              "EXPORTPROPERTYPLACEMENTSSCHEMAS", "IMPORTPROPERTYPLACEMENTSSCHEMAS",
              "REORGANIZE", "CORRECTPROJECTITEMS", "LOADDIRECTORY"
        project_name: Project path with full path - ask the user, do not guess.
        filename: Meaning varies by type - see notes above (XML source/target
              for READPROJECTINFO/EXPORT*/IMPORT*; base path with irrelevant
              extension for PUBLISHSMARTPRODUCTION/CREATESNAPSHOTCOPY)
        scheme: Scheme name - used by CREATESNAPSHOTCOPY and CORRECTPROJECTITEMS
        overwrite: Whether to overwrite existing schemes (0/1) - IMPORTPROPERTYPLACEMENTSSCHEMAS
        extended_mode: Enable extended mode for reorganize (0/1)
        projects_directory: Directory to scan for LOADDIRECTORY
        scan_subdirectories: Scan subdirectories (0/1, default 1)
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "projectmanagement",
        TYPE=type,
        PROJECTNAME=project_name,
        FILENAME=filename,
        SCHEME=scheme,
        OVERWRITE=overwrite,
        EXTENDEDMODE=extended_mode,
        PROJECTSDIRECTORY=projects_directory,
        SCANSUBDIRECTORIES=scan_subdirectories
    )
    return manager.execute_action(action)


def upgrade_projects(project_paths: List[str]) -> dict:
    """
    Upgrade projects to current database scheme version.
    Action: XPrjActionUpgradeProjects

    Args:
        project_paths: List of project paths to upgrade
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    # Build action with numbered project parameters
    parts = ["XPrjActionUpgradeProjects"]
    for i, path in enumerate(project_paths, 1):
        parts.append(f'/PROJECT{i}:"{path}"')

    return manager.execute_action(" ".join(parts))


def compress_project(project_name: str = None) -> dict:
    """
    Compress a project to reduce file size.
    Action: compress
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "compress",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def synchronize_project(project_name: str = None) -> dict:
    """
    Synchronize project data.
    Action: synchronize
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "synchronize",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def get_current_project() -> dict:
    """
    Get the current project path.
    Action: selectionset (TYPE:PROJECT)

    The result is returned in the calling context parameter "PROJECT"
    (full project path with .elk extension).

    IMPORTANT: This only reports whichever single project currently has
    focus/is active in EPLAN. If the user has multiple projects open at
    once, this tool cannot see or list the others - it will not tell you
    that more than one is open. Do not assume the returned project is the
    only one open; if it matters which projects are open, ask the user.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "selectionset",
        TYPE="PROJECT"
    )
    return manager.execute_action(action)


def set_project_language(
    language: str,
    project_name: str = None,
    read_write: bool = True
) -> dict:
    """
    Set project language.
    Action: SetProjectLanguage
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "SetProjectLanguage",
        PROJECTNAME=project_name,
        LANGUAGE=language,
        READWRITE="1" if read_write else "0"
    )
    return manager.execute_action(action)


def switch_project_type(
    project_type: str,
    project_name: str = None
) -> dict:
    """
    Change the type of project.
    Action: SwitchProjectType
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "SwitchProjectType",
        PROJECTNAME=project_name,
        PROJECTTYPE=project_type
    )
    return manager.execute_action(action)
