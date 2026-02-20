# projectmanagement

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/projectmanagement.html

---

```
Action class for project management.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed:
 '¢ "READPROJECTINFO": Load project information from an XML file into the project.
 '¢ "PUBLISHSMARTPRODUCTION": Publishes project for EPLAN Smart Production.
 '¢ "CREATESNAPSHOTCOPY": Creates snapshot copy of the project.
 '¢ "EXPORTPROPERTYPLACEMENTSSCHEMAS": Exports property placements schemes.
 '¢ "IMPORTPROPERTYPLACEMENTSSCHEMAS": Imports property placements schemes.
 '¢ "REORGANIZE": Reorganizes project.
 '¢ "CORRECTPROJECTITEMS": Corrects project items.
 '¢ "LOADDIRECTORY": Scans directory for projects to add them into the project management. This type can be used as "Stand-Alone" or with the Parameter: "PROJECTSDIRECTORY" and "SCANSUBDIRECTORIES"
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is call from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` FILENAME
 ``` | ``` Full path / name of the XML file to be imported, or full file path to be published,
 or full file path to target project when creating snapshot copy.
 ``` |
| ``` SCHEME
 ``` | ``` Name of the scheme. This parameter is only effective with the following values of the TYPE parameter: "CREATESNAPSHOTCOPY", "CORRECTPROJECTITEMS"
 ``` |
| ``` OVERWRITE
 ``` | ``` If the imported property placement scheme already exists, this parameter specifies whether it should be overwritten. 
 Possible values: 0 = No (default), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "IMPORTPROPERTYPLACEMENTSSCHEMAS"
 ``` |
| ``` EXTENDEDMODE
 ``` | ``` Enables extended mode while reorganizing the project.
 Possible values: 0 = No (default), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "REORGANIZE".
 ``` |
| ``` PROJECTSDIRECTORY
 ``` | ```  Path to directory which will be scanned. If null or empty then default path "USER.TrDMProject.Masterdata.Pathnames.Projects" is used.
 ``` |
| ``` SCANSUBDIRECTORIES
 ``` | ```  Determines whether sub directories are also scanned for projects.
 Possible values: 0 = No, 1 = Yes (default).
 ``` |

**Remarks**

```
The specified project may be open or closed. If the project is not open, it is opened when the process is started and closed after the export.

When an error occurs during a project management operation, a "BaseException" is thrown.

```

**Example**

```
projectmanagement /TYPE:READPROJECTINFO /PROJECTNAME:"C:\Projects\EPLAN\EPLAN_Sample_Project.elk" /FILENAME:C:\Files\ProjectInfo.xml

projectmanagement /TYPE:EXPORTPROPERTYPLACEMENTSSCHEMAS /PROJECTNAME:"C:\Projects\EPLAN\EPLAN_Sample_Project.elk" /FILENAME:C:\Files\PPSchemas.xml

projectmanagement /TYPE:IMPORTPROPERTYPLACEMENTSSCHEMAS /PROJECTNAME:"C:\Projects\EPLAN\EPLAN_Sample_Project.elk" /FILENAME:C:\Files\PPSchemas.xml /OVERWRITE:1

projectmanagement /TYPE:REORGANIZE /PROJECTNAME:"C:\Projects\EPLAN\EPLAN_Sample_Project.elk" /EXTENDEDMODE:1

projectmanagement /TYPE:CORRECTPROJECTITEMS /PROJECTNAME:"C:\Projects\EPLAN\EPLAN_Sample_Project.elk" /SCHEME:Default

projectmanagement /TYPE:LOADDIRECTORY /PROJECTSDIRECTORY:"C:\Projects\EPLAN" /SCANSUBDIRECTORIES:true

projectmanagement /TYPE:LOADDIRECTORY

```