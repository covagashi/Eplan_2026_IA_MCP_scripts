# Location Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~Location.html

---

Get or set the placement's location.

Syntax

**C#**



public override PointD Location {get; set;}

public:

property PointD Location {

   PointD get() override;

   void set (    PointD value) override;

}


#### Property Value

Current location of the placement.

Exceptions

| Exception | Description |
| --- | --- |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when property or function can not be used for specific class. For example it is thrown when this property is called on [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) objects. |

Remarks

In case of SymbolReferences, location is just an insertion point of a SymbolReference in graphical coordinate system. Please use CoordinateService class in order to recalculate to another coordinate systems. When the location is changed (and the symbol is moved) then it is possible that some automatic connections will be disconnected or connected differently.
