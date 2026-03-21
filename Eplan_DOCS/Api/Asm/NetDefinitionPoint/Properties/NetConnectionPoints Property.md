# NetConnectionPoints Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint~NetConnectionPoints.html

---

Returns all PinBase objects of NetDefinitionPoint

Syntax

**C#**



public NetDefinitionPoint.NetConnectionPoint[] NetConnectionPoints {get;}

public:

property array<NetDefinitionPoint.NetConnectionPoint^>^ NetConnectionPoints {

   array<NetDefinitionPoint.NetConnectionPoint^>^ get();

}


#### Property Value

All PinBases defined in NetDefinitionPoint

Remarks

`NetConnectionPoints` are [PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)s taken from [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html). Location of `NetConnectionPoints` is relative to the symbol's insertion point.
