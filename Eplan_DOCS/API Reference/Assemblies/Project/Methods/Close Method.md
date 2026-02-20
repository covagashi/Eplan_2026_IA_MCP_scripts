# Close Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Close.html

---

Closes the project. Must not be called before Remove()

Syntax

**C#**



public void Close()

public:

void Close();


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project was already closed. |

Remarks

Warning: exception [ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) is thrown when getting/setting properties or calling methods (except [ProjectManager.OpenProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~OpenProject(String).html)) on closed project.
