# preparemacros

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/preparemacros.html

---

```
Action for preparing project for macro generation.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` PAGENAMEn
 ``` | ``` Names of the pages to be considered (optional), where n is a number e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc. 
 ``` |
| ``` GroupMacroBoxes
 ``` | ``` Group macro boxes with their content.
 Possible values: 0 = "Do nothing", 1 = "Create Groups" (default).
 ``` |
| ``` GroupPageMacros
 ``` | ``` Group content of a page macro.
 Possible values: 0 = "Do nothing" (default), 1 = "Create Groups".
 ``` |
| ``` SetHandleActive
 ``` | ``` Set handle checkbox active.
 Possible values: 0 = "Do nothing" (default), 1 = "Activate handle checkbox".
 ``` |

**Remarks**

```
       

Project must have property "Type of project" set to "Macro project".                    

```

**Example**

```
Macros preparation

preparemacros /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

```