# GetProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProject.html

---

Gets an already open project.

Syntax

**C#**



public Project GetProject( 

   string linkFileName

)

public:

Project^ GetProject( 

   String^ linkFileName

)


#### Parameters

*linkFileName*
:   Full link file name "C:\\Eplan\\P8\\Projects\\EPLAN\_Sample\_Project.elk"

#### Return Value

Project : project object or null

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if the source project does not exist |
| [System.ArgumentNullException](#) | Thrown when `linkFileName` is `null`. |
| [ProjectLockingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectLockingException.html) | Thrown when [LockProjectByDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~LockProjectByDefault.html) is `true` and a project cannot be locked. |

Remarks

if the project is not already open, this method returns null This method works with a project and embedded libraries: project settings, symbol libraries and the function libraries.
