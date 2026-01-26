# Location Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Location.html

---

Get or set the placement's location.

Syntax

**C#**



public virtual PointD Location {get; set;}

public:

virtual property PointD Location {

   PointD get();

   void set (    PointD value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when property or function can not be used for specific class. For example it is thrown when this property is called on [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) objects. |
