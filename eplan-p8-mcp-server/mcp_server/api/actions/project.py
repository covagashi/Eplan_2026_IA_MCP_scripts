"""
Project management actions.
"""

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

    To create a copy/duplicate of a project (e.g. "make a copy of X",
    "duplicate this project"), use type="CREATESNAPSHOTCOPY" - see its
    entry below for exact parameters. It is the correct tool for that
    request, not a file-system copy of the .elk/.edb.

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
      FROM an XML file INTO the project (a write). It reads project info
      formatted as EPLAN's own "ProjectInfo.xml" - every project already
      has one of these, sitting inside its `.edb` folder at
      `<project>.edb\\ProjectInfo.xml`. In practice `filename` should point
      at that file, either from the same project (self-referential
      refresh) or copied from a different project's `.edb` folder if the
      goal is to bring in that project's info. Feeding it an XML of a
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
      shrank measurably. Always confirm with the user before calling. Not
      to be confused with the separate compress_project tool, which also
      reduces project file size but by removing unused macros/parts instead
      of purging already-deleted data - different mechanism, different tool.

    - "CORRECTPROJECTITEMS": designed to automatically correct, synchronize,
      and repair inconsistent elements/data within a project. Takes
      `scheme` (e.g. "Default" per official docs example). Irreversible-ish
      modification, confirm with the user first. Confirmed success:true can
      happen with zero observable effect on disk - don't assume it changed
      anything without checking. Despite the official docs using the word
      "synchronize" here, this is unrelated to the separate
      synchronize_project tool (which syncs the parts/system database) - if
      the user wants to "synchronize" parts data, they most likely mean
      synchronize_project, not this.

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


def upgrade_projects(project_path: str = None, folder_path: str = None) -> dict:
    """
    Upgrade project(s) to the current database scheme version.
    Action: XPrjActionUpgradeProjects

    Pass exactly one of the two arguments:
    - project_path: upgrade a single project file (e.g. a .elk file).
    - folder_path: upgrade every project found in this folder and all its
      subfolders (recursive).

    Always ask the user for the exact path first (which project file, or
    which folder) - do not guess it. This action changes the project's
    database scheme and is effectively irreversible for that copy, so
    confirm with the user before each call, and tell them the outcome
    afterward.

    Behavior:
    - A backup of each project is created automatically before upgrading;
      this wrapper does not expose a way to disable that.
    - Does nothing (still reports success) for a project that is already on
      the current scheme version.
    - Basic projects (ZW9/ZX1) are only upgraded on a major version change.
    - The result only echoes back what was sent (success + parameters). It
      does NOT include EPLAN's own per-project result message - that stays in
      EPLAN's message/log window. If success is false, there is no
      diagnostic detail available here or from eplan_status; check EPLAN's
      message window directly for the reason.

    Args:
        project_path: Full path to a single project file to upgrade.
        folder_path: Full path to a folder whose projects (recursively)
            should all be upgraded.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    if project_path and folder_path:
        return {"success": False, "error": "Pass only one of project_path or folder_path, not both."}
    if folder_path:
        return manager.execute_action(f'XPrjActionUpgradeProjects /Folder:"{folder_path}"')
    if project_path:
        return manager.execute_action(f'XPrjActionUpgradeProjects /Project:"{project_path}"')
    return {"success": False, "error": "Must provide either project_path or folder_path."}


def compress_project(project_name: str = None) -> dict:
    """
    Compress a project to reduce its file size.
    Action: compress

    Removes macros and articles (parts) that are not actually used anywhere
    in the project - it is a cleanup of unused embedded data, not a
    reorganize/defragment of the database and not a zip-style archive. Ask
    the user for the project path if it's not obvious which project they
    mean; if project_name is omitted, behavior is unconfirmed (may target
    whichever project currently has focus in the EPLAN GUI, similar to
    close_project).
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "compress",
        PROJECTNAME=project_name
    )
    return manager.execute_action(action)


def synchronize_project(project_name: str = None, type: str = None, store_mode: int = None) -> dict:
    """
    Synchronize project data with the EPLAN parts/system database.
    Action: synchronize

    Not to be confused with project_management's CORRECTPROJECTITEMS type,
    whose official EPLAN description also happens to use the word
    "synchronize" but which does unrelated data-consistency repair, not
    parts-database sync. If the user wants to sync parts between a project
    and the shared system database, this tool is the right one.

    Always ask the user for the exact project_name (full path) before
    calling - never omit it and never guess it. The underlying EPLAN action
    treats PROJECTNAME as optional and falls back to whichever project has
    focus in the GUI, but that fallback only works when the action is
    triggered from inside the GUI (script/ribbon bar); when invoked
    programmatically like this MCP server does, omitting it throws an
    exception instead of defaulting sensibly.

    Args:
        project_name: Project name with full path. Ask the user - do not
            guess or omit.
        type: Type of synchronization task to perform:
            "MULTILINE": Multi-line data synchronization.
            "SINGLELINE": Single-line data synchronization.
            "OVERVIEW": Overview data synchronization.
            "SYSTEMPARTSTOPROJECT": Add system (shared) parts to this project.
            "PARTSTOSYSTEM": Add this project's parts to the shared system
                parts database - unlike the other TYPE values this writes to
                data shared across every project on this EPLAN installation,
                not just the one project passed in. Treat it as
                higher-impact and confirm with the user before running it,
                especially against a project that may contain throwaway/test
                parts. If the system parts database is write-protected or
                locked (e.g. another EPLAN session/process has it open, or
                it's a read-only master data source), this fails with
                `{"success": false}` and no error detail anywhere in this
                MCP (not in the result, not in eplan_status) - the real
                reason only shows in EPLAN's own message window (seen in
                practice as "La base de datos está protegida contra
                escritura" / "The database is write protected"). If this
                TYPE fails, don't assume the call itself was malformed -
                tell the user to check EPLAN's message window, and that a
                locked/protected system parts database is a likely cause.
        store_mode: Only effective when type="SYSTEMPARTSTOPROJECT". Whether
            existing parts are overwritten:
            0: Append only new ones (default).
            1: Overwrite existing.
            2: Overwrite existing and append new.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "synchronize",
        TYPE=type,
        PROJECTNAME=project_name,
        STOREMODE=store_mode
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
    display: str,
    project_name: str = None,
    variable: str = None,
    source: str = None
) -> dict:
    """
    Set which language(s) a project displays, and which one is active.
    Action: SetProjectLanguage

    This does NOT translate any text - it only changes display settings
    (which language(s) show, and which one is currently active/edited). The
    project must already be open in EPLAN; ask the user for the exact
    project_name if more than one project could be open.

    Args:
        display: Displayed language ID(s), e.g. "en_US". To display more
            than one language at once, separate IDs with ";", e.g.
            "en_US;de_DE;pl_PL;fr_FR".
        project_name: Full project name/path. The project must be open.
        variable: The "variable" (currently active) language. Either a
            language ID directly (e.g. "de_DE"), or a positional index into
            `display` written as "0N_0N" (e.g. "03_03" for "Displayed
            language 3"). The index form only works for the first 5
            displayed languages - "05_05" is the maximum.
        source: Source language.
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    action = _build_action(
        "SetProjectLanguage",
        PROJECTNAME=project_name,
        DISPLAY=display,
        VARIABLE=variable,
        SOURCE=source
    )
    return manager.execute_action(action)


def switch_project_type(
    project_type: int,
    project_name: str = None
) -> dict:
    """
    Change a project's type.
    Action: SwitchProjectType

    EPLAN projects are only ever one of two types:
        1 = Schematic project
        2 = Macro project

    Always ask the user both which project (project_name) and which type
    they want to switch to - never guess or assume either. The underlying
    EPLAN action technically treats both as optional, but the fallbacks are
    not safe to rely on here: omitting project_type does NOT no-op, it
    toggles the project to whichever of the two types it is NOT currently
    set to; omitting project_name falls back to whichever project has
    focus in the GUI, but that fallback only works when triggered from
    inside the GUI, not when called programmatically like this MCP server
    does (it throws an exception instead). So always pass both explicitly.

    This is a structural change to the project - confirm with the user
    before calling.

    Args:
        project_type: 1 for Schematic project, 2 for Macro project. Ask the
            user - do not guess or default to either.
        project_name: Full project path. Ask the user - do not guess.
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
