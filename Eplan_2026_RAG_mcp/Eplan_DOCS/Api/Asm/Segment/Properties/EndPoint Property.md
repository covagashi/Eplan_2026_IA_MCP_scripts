# EndPoint Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment~EndPoint.html

---

Returns end point of this segment.

Syntax

**C#**



public PointD EndPoint {get; set;}

public:

property PointD EndPoint {

   PointD get();

   void set (    PointD value);

}


#### Property Value

[Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) - start point of this segment.

Remarks

This property is automatically updated by methods Eplan.EplApi.HEServices.TopologyService.UpdatePage() or Eplan.EplApi.HEServices.TopologyService.UpdateTopologySegment() if [EndSymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment~EndSymbolReference.html) is set.
