# restore

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/restore.html

---

```
Action class for restore functions: restore projects and restore master data (forms, symbols, ...)

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed:
 "PROJECT": Restore project
 "MASTERDATA": Restore master data
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path.This only applies to TYPE value "PROJECT".
 ``` |
| ``` ARCHIVENAME
 ``` | ``` Archive name. Name of the  archive to be restored.
 ``` |
| ``` DESTINATIONPATH
 ``` | ``` Target directory. Path where the projects or data are to be restored.
 Only applies to TYPE value "MASTERDATA".
 ``` |
| ``` UNPACKPROJECT
 ``` | ``` Specifies whether the previously packed project is to be unpacked (optional, 1 = Yes, 0 = No). 
 Set this flag to 0, only if previously packed projects are to be unpacked,
 Default value = 0
 Only applies to TYPE value "PROJECT".
 ``` |
| ``` MODE
 ``` | ``` If set to 0, project information file (ProjectInfo.xml) will not be restored (optional).
 Default value = 1
 Only applies to TYPE value "PROJECT".
 ``` |

**Remarks**

```
Restored project is automatically upgraded to the currently used EPLAN version.

When an error occurs during a restore operation, a "BaseException" is thrown.

In case of invalid arguments or when parameter arguments are missing (e.g. the project name is missing), a "System::ArgumentException" is thrown.

```

**Example**

```
Restore project:

restore /TYPE:PROJECT /ARCHIVENAME:C:\temp\EPLAN_Sample_Project.zw1 /PROJECTNAME:C:\temp\EPLAN_Sample_Project.elk /UNPACKPROJECT:0

Restore master data (plot frames, ...) to a DestinationPath

restore /TYPE:MASTERDATA /ARCHIVENAME:C:\temp\EPLAN_Sample_Project.zw2 /DESTINATIONPATH:C:\temp

```