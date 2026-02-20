# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~Remove.html

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
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when object has not been created yet. |

Remarks

This method enables the user to delete objects which sometimes cannot be removed from a project. For example, selecting some device from a list view in GUI and deleting it will not be possible. However, the same object can be deleted by calling the above method.
