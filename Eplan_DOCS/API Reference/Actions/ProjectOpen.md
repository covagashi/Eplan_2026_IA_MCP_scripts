# ProjectOpen

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ProjectOpen.html

---

```
 Opens given project.

```

| Parameter | Description |
| --- | --- |
| ``` Project
 ``` | ``` Project to be opened
 ``` |
| ``` OpenMode
 ``` | ``` Specifies the mode in which the project is opened (optional). May have the following values: "Standard", "ReadOnly", "Exclusive".
 ``` |

**Remarks**

```
 * When the OpenMode is specified, the project is opened in this mode or not opened at all, then an error is reported.

 * When the OpenMode is NOT specified, the system tries to open the project in Standard mode (readable and writable).

 When the project needs an upgrade, it is opened in ReadOnly mode (or not opened at all, then an error is reported).

 The actual open mode is added to the calling context with the parameter "OpenMode".

```

**Example**

```
        ProjectOpen /Project:C:\EPLAN\Projects\EPLAN_Sample_Project.elk

        ProjectOpen /Project:"C:\EPLAN\my own Projects\EPLAN_Sample_Project.elk"

```