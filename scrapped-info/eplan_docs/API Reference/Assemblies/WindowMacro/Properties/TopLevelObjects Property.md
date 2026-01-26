# TopLevelObjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~TopLevelObjects.html

---

Returns all Eplan.EplApi.DataModel.Placements, with no parent.

Syntax

**C#**



public Placement[] TopLevelObjects {get;}

public:

property array<Placement^>^ TopLevelObjects {

   array<Placement^>^ get();

}


#### Property Value

[Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)

Remarks

This array include Eplan.EplApi.DataModel.Group objects.
