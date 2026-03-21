# SubPlacements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~SubPlacements.html

---

Returns all grouped [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s.

Syntax

**C#**



public virtual Placement[] SubPlacements {get; set;}

public:

virtual property array<Placement^>^ SubPlacements {

   array<Placement^>^ get();

   void set (    array<Placement^>^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read grouped placements. |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when property or function can not be used for specific class. |
