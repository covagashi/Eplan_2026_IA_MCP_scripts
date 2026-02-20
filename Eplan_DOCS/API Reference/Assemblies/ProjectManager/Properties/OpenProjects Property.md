# OpenProjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~OpenProjects.html

---

Returns list of all open projects.

Syntax

**C#**



public Project[] OpenProjects {get;}

public:

property array<Project^>^ OpenProjects {

   array<Project^>^ get();

}


#### Property Value

Array of all open [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)s. When there are no open projects, a 0-size array is returned.

Exceptions

| Exception | Description |
| --- | --- |
| [ProjectLockingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectLockingException.html) | Thrown when [LockProjectByDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~LockProjectByDefault.html) is `true` and a project cannot be locked. |

Remarks

If LockProjectByDefault is set to true, OpenProjects tries to lock the returned projects. If not all open projects can be locked, OpenProjects throws a ProjectLockingException. Please consider this if you work with e.g. write-protected or revisioned projects.
