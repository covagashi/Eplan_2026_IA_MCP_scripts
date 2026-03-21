# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Remove.html

---

Removes placement.

Syntax

**C#**



public override void Remove()

public:

void Remove(); override


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to remove the group. Thrown by internal method. |
| [RemoveFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.RemoveFailedException.html) | Thrown when it is impossible to remove the group. Thrown by API DataModel. |

Remarks

This method enables the user to delete objects which sometimes cannot be removed from a project. For example, selecting some device from a list view in GUI and deleting it will not be possible. However, the same object can be deleted by calling the above method.
