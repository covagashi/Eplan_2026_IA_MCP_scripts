# masterdata

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/masterdata.html

---

```
Action class for operations related to EPLAN master data.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 UPDATEPROJECT: Updates project master data
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |

**Example**

```
Update project master data from system

masterdata /TYPE:UPDATEPROJECT

```