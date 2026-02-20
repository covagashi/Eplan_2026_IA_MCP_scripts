# OpenProject(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~OpenProject(String).html

---

Opens a project.

Syntax

**C#**



public Project OpenProject( 

   string linkFileName

)

public:

Project^ OpenProject( 

   String^ linkFileName

)


#### Parameters

*linkFileName*
:   Full link file name "C:\\Eplan\\P8\\Projects\\EPLAN\_Sample\_Project.elk"

#### Return Value

Project : project object

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if the source project does not exist |
| [System.ArgumentNullException](#) | Thrown when `linkFileName` is `null`. |
| [ProjectOpenException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectOpenException.html) | Thrown when requested project cannot be open |
| [ProjectLockingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectLockingException.html) | Thrown when [LockProjectByDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~LockProjectByDefault.html) is `true` and a project cannot be locked. |
| [ProjectNeedsUpgradeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNeedsUpgradeException.html) | Thrown when project  `linkFileName`  has old database structure and needs to be upgraded. |
| [IncompatibleDatabaseException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncompatibleDatabaseException.html) | Thrown when project  `linkFileName`  has incompatible database structure and we can do nothing about it. |

Remarks

This method works with a project and embedded libraries: project settings, symbol libraries and the function libraries. If the project is read-only (for example it is stored on a read-only drive) or number of logical pages exceeds number of licensed logical pages the project hierarchy will be opened read-only. Otherwise the project will be open read-write or exclusive, depending on available multi-user licenses. The embedded libraries always are opened read-only. Projects created by EPLAN versions lower than 2.4 need to be upgraded, otherwise an exception is thrown. If project it is an outsourced (.els files) or packed (.elp files) it can be opened by this function. In case of backed-up projects please use Eplan.EplApi.HEServices.Restore class.
