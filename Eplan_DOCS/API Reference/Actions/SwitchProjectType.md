# SwitchProjectType

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/SwitchProjectType.html

---

```
Action to change type of project.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected  project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` PROJECTTYPE
 ``` | ``` New type of project (optional). Type is represented by numbers: 
 1 - Schematic project; 
 2 - Macro project. 
 If this parameter is not used then action will switch current type to the second.
 ``` |

**Example**

```
Switch project type to Macro:

SwitchProjectType /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PROJECTTYPE:2

```