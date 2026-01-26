# CurrentProject Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CurrentProject.html

---

ProjectManager's property which returns first project from the list of opened projects. Please use Eplan::EplApi::HeServices::SelectionSet class in order to get the selected project, or other selected objects.

Syntax

**C#**



public Project CurrentProject {get;}

public:

property Project^ CurrentProject {

   Project^ get();

}


#### Property Value

First opened [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html), or when there are no projects opened `null` is returned.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exception is thrown, when current project is not locked and cannot be locked. |
| [ProjectLockingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectLockingException.html) | Thrown when [LockProjectByDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~LockProjectByDefault.html) is `true` and a project cannot be locked. |
| [InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when current project is invalid. |
