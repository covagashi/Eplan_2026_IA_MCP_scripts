# SaveWorkspaceAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/SaveWorkspaceAction.html

---

```
 Saves the specified workspace. If the workspace already exists, changes are saved. If the workspace does not yet exist, it is created and saved.

```

| Parameter | Description |
| --- | --- |
| ``` Workspacename
 ``` | ``` Name of the workspace to be saved (a string).
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
 The following example will save the "Standard" workspace:

 SaveWorkspaceAction /Workspacename:Standard

```