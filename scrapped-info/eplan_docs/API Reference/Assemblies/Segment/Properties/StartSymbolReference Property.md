# StartSymbolReference Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment~StartSymbolReference.html

---

Returns the first of two [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this segment.

Syntax

**C#**



public SymbolReference StartSymbolReference {get; set;}

public:

property SymbolReference^ StartSymbolReference {

   SymbolReference^ get();

   void set (    SymbolReference^ value);

}


#### Property Value

- the first of two [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this segment,
- `null` when there is no SymbolReference on this side of the segment.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the SymbolReference from project. |

Remarks

After setting value to this property the [StartPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment~StartPoint.html) position is not automaticly updated. To update it, please use method UpdatePage() or UpdateTopologySegment of class Eplan.EplApi.HEServices.TopologyService.
