# GetProjectDatabaseVersion Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProjectDatabaseVersion.html

---

Project database version.

Syntax

**C#**



public ProjectManager.DatabaseVersion GetProjectDatabaseVersion( 

   string projectPath

)

public:

ProjectManager.DatabaseVersion^ GetProjectDatabaseVersion( 

   String^ projectPath

)


#### Parameters

*projectPath*
:   Path to .elk project file.

Exceptions

| Exception | Description |
| --- | --- |
| [ProjectNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNotFoundException.html) | Thrown when project doesn't exist. |
| [ProjectOpenException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectOpenException.html) | Thrown when requested project cannot be open |
| [System.ArgumentNullException](#) | Thrown when  `projectPath`  is `null`. |
