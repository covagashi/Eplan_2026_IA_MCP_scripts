# compress

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/compress.html

---

```
Action class to compress projects.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` CONFIGSCHEME
 ``` | ``` Configuration scheme for project compression (optional).
 Default value: Recent configuration     scheme. The most recently used scheme is taken if an empty string is passed. 
 ``` |

**Remarks**

```
When an error occurs during a compress operation, a "BaseException" is thrown.

```

**Example**

```
Compress a project.

compress /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /CONFIGSCHEME:config_scheme

Use the most recent configuration scheme: The 'CONFIGSCHEME' parameter is not entered.

compress /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

```