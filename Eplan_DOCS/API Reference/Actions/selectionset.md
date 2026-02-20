# selectionset

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/selectionset.html

---

```
Action class for selection set functions: get current project, get selected projects, get selected pages.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed:
 "PROJECT": Return current project
 "PROJECTS": Return selected projects
 "PAGES": Return selected pages
 "LAYOUTSPACES": Return selected layout spaces
 ``` |

**Remarks**

```
The results of the selection are returned in the CallingContext.

Current project:

Parameter name in calling context = "PROJECT";

Values from calling context = full project name with path and file extension (e.g. "C:\MyProjects\EPLAN_Sample_Project.elk").

If projects are selected:

Parameter name in calling context = "PROJECTS";

Values from calling context = full project names with path and file extension separated by ";" (e.g. "C:\MyProjects\EPLAN_Sample_Project.elk;C:\Projects\EPLAN\EPLAN_Sample_Project2.elk").

If pages are selected:

Parameter name in calling context = "PAGES";

Values from calling context = all page names separated by ";", e.g. "Page1;Page2;Page3"

If layout spaces are selected:

Parameter name in calling context = "LAYOUTSPACES";

Values from calling context = all layout spaces are separated by ";", e.g. "LayoutSpace1; LayoutSpace2; LayoutSpace3"

When an error occurs during a selection set operation, a "BaseException" is thrown.

```

**Example**

```
Return current project:

selectionset  /TYPE:PROJECT

Results in calling context: Parameter name = "PROJECT"

Value = "C:\Projects\EPLAN\EPLAN_Sample_Project.elk"

Return currently selected projects:

selectionset  /TYPE:PROJECTS

Results in calling context: Parameter name = "PROJECTS"

Value = "C:\Projects\EPLAN\EPLAN_Sample_Project.elk;C:\Projects\EPLAN\EPLAN_Sample_Project2.elk"

Return currently selected pages:

selectionset  /TYPE:PAGES

Results in calling context: Parameter name = "PAGES"

Value = "=AP+ST1/1;=AP+ST1/2;=AP+ST1/5"

Return currently selected layout spaces:

selectionset  /TYPE:LAYOUTSPACES

Results in calling context: Parameter name = "LAYOUTSPACES"

Value = "A1;A2;A3"

```