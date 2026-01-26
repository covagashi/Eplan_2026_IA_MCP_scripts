# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~Remove.html

---

Removes the 3D group and all grouped [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s.

Syntax

**C#**



public virtual void Remove()

public:

virtual void Remove();


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to remove the Group3D object. Thrown by internal method. |
| [Eplan.EplApi.DataModel.RemoveFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.RemoveFailedException.html) | Thrown when it is impossible to remove the Group3D object. Thrown by API DataModel. |
