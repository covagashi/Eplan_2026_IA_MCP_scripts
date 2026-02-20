# UpdateProjectStructureFromSettings Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~UpdateProjectStructureFromSettings.html

---

Updates project structure for navigator (GUI) according to the project settings.

Syntax

**C#**



public void UpdateProjectStructureFromSettings( 

   Project oProject

)

public:

void UpdateProjectStructureFromSettings( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project to be updated.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if oProject is NULL. |
| [System.ApplicationException](#) | Thrown if oProject is an invalid project. |
| [System.ApplicationException](#) | Thrown if structure of oProject could not be updated according to the project settings. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |

Remarks

This function matches the project structure to the database, depending on the current project settings. For this operation, the given project is temporarily opened in exclusive lock mode.
