# graphicallayertable

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/graphicallayertable.html

---

```
Action class for graphical layer table functions: import, export.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "IMPORT": Import graphical layer table
 '¢ "EXPORT": Export graphical layer table
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path(optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` IMPORTFILE
 ``` | ``` The directory and the file name of the table to be imported must be specified here.
 ``` |
| ``` EXPORTFILE
 ``` | ``` The directory and the file name of the table to be exported must be specified here.
 ``` |

**Remarks**

```
When an error occurs during a graphical layer table operation, a "BaseException" is thrown.

```

**Example**

```
Import:

graphicallayertable /TYPE:IMPORT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /IMPORTFILE:C:\EPLAN\EPLAN_Sample_Project.elc

Export:

graphicallayertable /TYPE:EXPORT /PROJECTNAME:C:\Projekte\EPLAN\EPLAN_Sample_Project.elk /EXPORTFILE:C:\EPLAN\EPLAN_Sample_Project.elc

```