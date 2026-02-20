# PropertyPlacements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacements.html

---

Returns [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the SymbolReference.

Syntax

**C#**



public virtual PropertyPlacement[] PropertyPlacements {get;}

public:

virtual property array<PropertyPlacement^>^ PropertyPlacements {

   array<PropertyPlacement^>^ get();

}


#### Property Value

[Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the SymbolReference.

Remarks

When a new object was created by API, the displayed properties are set from original default scheme of the symbol, even if another was set as default by user. Please use property SymbolReference.PropertyPlacementsSchemas.Selected to change displayed properties scheme.
