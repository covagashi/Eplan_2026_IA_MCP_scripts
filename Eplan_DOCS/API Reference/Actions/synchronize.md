# synchronize

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/synchronize.html

---

```
Action class to synchronize project data.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of synchronization task to be performed:
 "MULTILINE": Multi-line data synchronization.
 "SINGLELINE":Single-line data synchronization.
 "OVERVIEW": Overview data synchronization.
 "SYSTEMPARTSTOPROJECT": Add system parts to your project.
 "PARTSTOSYSTEM": Add parts of the project to the system.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` STOREMODE
 ``` | ``` Specifies whether existing parts are overwritten or only new ones added (optional). 
 0: Append only new ones (default value).
 1: Overwrite existing.
 2: Overwrite existing and append new.
 This parameter is only effective with the following value of the TYPE parameter: "SYSTEMPARTSTOPROJECT".
 ``` |

**Remarks**

```
This action can be used to synchronize multi-line, single-line and overview project data, as well as to synchronize the system parts with the project and vice versa.

```

**Example**

```
Synchronize parts to system database:

synchronize /TYPE:PARTSTOSYSTEM /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

```