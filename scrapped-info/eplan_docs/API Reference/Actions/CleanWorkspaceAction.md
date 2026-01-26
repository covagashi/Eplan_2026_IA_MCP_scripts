# CleanWorkspaceAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/CleanWorkspaceAction.html

---

```
 Cleans an existing workspace.

```

| Parameter | Description |
| --- | --- |
| ``` Workspacename
 ``` | ``` Name of the workspace to be cleaned (a string).
  If the workspace name is empty the LAST_USED workspace will be cleaned.
 ``` |
| ``` Silent
 ``` | ``` Determines whether it runs in silent mode (0 = No, 1 = Yes).
  In silent mode, all dialogs will be suppressed (e.g. error dialogs).
  Default = 0
 ``` |

**Remarks**

```
 This action needs a mainframe.

```

**Example**

```
 CleanWorkspaceAction /Workspacename:"?"

```