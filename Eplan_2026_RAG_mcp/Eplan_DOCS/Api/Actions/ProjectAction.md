# ProjectAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ProjectAction.html

---

```
 Runs an action upon a given project and closes project afterwards.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path
 ``` |
| ``` Action
 ``` | ``` Action to be executed, action parameter following.
 ``` |
| ``` NOCLOSE
 ``` | ``` Determines whether the current project will be closed afterwards (optional).
  0 = Project will be closed afterwards (default),
  1 = Project will not be closed afterwards
 ``` |
| ``` OpenMode
 ``` | ``` Specifies the mode in which the project is opened (optional). May have the following values: "Standard", "ReadOnly", "Exclusive".
 ``` |
| ``` EnableDialogs
 ``` | ``` When status is set to "TRUE", value passed in Action parameter won't start in quiet mode.
 ``` |

**Remarks**

```
Without parameter "Project" last opend project will be used.

 * When the OpenMode is specified, the project is opened in this mode or not opened at all, then an error is reported.

 * When the OpenMode is NOT specified, the system tries to open the project in Standard mode (readable and writable).

 When the project needs an upgrade, it is opened in ReadOnly mode (or not opened at all, then an error is reported).

 The actual open mode is added to the calling context with the parameter "OpenMode".

```

**Example**

```
        ProjectAction /PROJECTNAME:C:\Projects\EPLAN_Sample_Project.elk /Action:export /TYPE:PDFPROJECT /EXPORTFILE:C:\pdf\export.pdf

```