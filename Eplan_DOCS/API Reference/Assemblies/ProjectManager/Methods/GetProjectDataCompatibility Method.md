# GetProjectDataCompatibility Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProjectDataCompatibility.html

---

Compares database schemes from current and given project. In the result of this check project could ok , need upgrade or just be incompatible.

Syntax

**C#**



public ProjectManager.DatabaseVersion.Status GetProjectDataCompatibility( 

   string projectPath

)

public:

ProjectManager.DatabaseVersion.Status GetProjectDataCompatibility( 

   String^ projectPath

)


#### Parameters

*projectPath*
:   Path to .elk project file.

#### Return Value

Returned value is status of project database.

Exceptions

| Exception | Description |
| --- | --- |
| [ProjectNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNotFoundException.html) | Thrown when project doesn't exist. |
| [System.ArgumentNullException](#) | Thrown when  `projectPath`  is `null`. |
