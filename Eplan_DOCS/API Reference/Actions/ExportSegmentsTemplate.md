# ExportSegmentsTemplate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExportSegmentsTemplate.html

---

```
Action to export segment templates to file.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` FILENAME
 ``` | ``` Full file name of target file. Can't be null or empty.
 ``` |
| ``` DESCRIPTION
 ``` | ``` Description which is contained in exported file. Value should be in multilang string format.
 ``` |

**Example**

```
Export segments template with description to a file:

ExportSegmentsTemplate /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /FILENAME:C:\temp.xml /DESCRIPTION:Some_description

```