# XEsUserPropertiesImportAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsUserPropertiesImportAction.html

---

```
 Imports user properties to project from file.

```

| Parameter | Description |
| --- | --- |
| ``` XMLFile
 ``` | ``` Full path of the XML file (optional). If missing, a file selection dialog is shown.
 ``` |
| ``` Project
 ``` | ``` Full project name (optional). If missing, the selected project is taken or a project selection dialog is shown.
 ``` |
| ``` Overwrite
 ``` | ``` Overwrite existing properties (optional, default is a dialog to ask the user).
 ``` |

**Example**

```
 XEsUserPropertiesImportAction /XMLFile:c:\my_user.xml  /Project:c:\...\EPLAN_Sample_Project.elk

```