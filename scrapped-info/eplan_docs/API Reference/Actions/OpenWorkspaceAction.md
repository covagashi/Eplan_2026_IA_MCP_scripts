# OpenWorkspaceAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/OpenWorkspaceAction.html

---

```
 Opens an existing workspace.

```

| Parameter | Description |
| --- | --- |
| ``` Workspacename
 ``` | ``` Name of the workspace to be opened (a string).
 ``` |
| ``` Silent
 ``` | ``` Determines whether it runs in silent mode (optional, 0 = No, 1 = Yes).
  In silent mode, all dialogs will be suppressed (e.g. error dialogs).
  Default = 0
 ``` |

**Remarks**

```
 This action needs a mainframe.

```

**Example**

```
 The following example will open the "Standard" workspace:

 OpenWorkspaceAction /Workspacename:Standard

 The following example will show a list of all available workspaces in a messagebox:

 OpenWorkspaceAction /Workspacename:? /Silent:0

```