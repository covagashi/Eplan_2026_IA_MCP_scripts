# subprojects

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/subprojects.html

---

```
Action class to export and import subprojects.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed: 
 "FILEOFF": Export subproject action. "STORE": Import subproject action.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set. The project has to be opened in exclusive mode.
 After calling this method, the source project object becomes invalid (in "FILEOFF" type).
 ``` |
| ``` DESTINATIONPATH
 ``` | ``` Target directory (optional). Default value is "$(MD_PROJECTS)". Only used by "FILEOFF" type.
 ``` |
| ``` SPNR
 ``` | ``` Subproject number.
 ``` |
| ``` EXTENDONLY
 ``` | ``` Extend subproject only (optional). Default value is "FALSE". Only used by "FILEOFF" type.
 ``` |
| ``` SUBPROJECTDIR
 ``` | ``` Directory where subproject is placed (optional). Default value is taken from alias. Only used by "STORE" type.
 ``` |

**Remarks**

```
When an error occurs during a subprojects operation, a "BaseException" is thrown.

When the project or any other parameter is invalid, a "System.ArgumentException" is thrown.

```

**Example**

```
Export subproject:

subprojects /TYPE:FILEOFF /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /SPNR:1

Import subproject:

subprojects /TYPE:STORE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /SPNR:1 /SUBPROJECTDIR:C:\Projects\Subprojects

```