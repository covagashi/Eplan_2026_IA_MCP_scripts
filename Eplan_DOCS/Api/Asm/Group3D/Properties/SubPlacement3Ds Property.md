# SubPlacement3Ds Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~SubPlacement3Ds.html

---

Returns all grouped [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s.

Syntax

**C#**



public virtual Placement3D[] SubPlacement3Ds {get; set;}

public:

virtual property array<Placement3D^>^ SubPlacement3Ds {

   array<Placement3D^>^ get();

   void set (    array<Placement3D^>^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read grouped 3D placements. |
| [Eplan.EplApi.DataModel.ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when property or function can not be used for specific class. |
