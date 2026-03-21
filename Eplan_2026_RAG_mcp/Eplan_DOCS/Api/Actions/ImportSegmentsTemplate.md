# ImportSegmentsTemplate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ImportSegmentsTemplate.html

---

```
Action to import segment templates from file to project.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path(optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` FILENAME
 ``` | ``` Full file name of source file. Can't be null or empty.
 ``` |

**Example**

```
Import segments template from file:

ImportSegmentsTemplate /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /FILENAME:C:\temp.xml

```