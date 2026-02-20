# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Remove.html

---

Removes the connection from the [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html).

Syntax

**C#**



public virtual void Remove()

public:

virtual void Remove();


Exceptions

| Exception | Description |
| --- | --- |
| [RemoveFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.RemoveFailedException.html) | Thrown when it is impossible to remove the connection, i.e. IsRemovable return false. |
