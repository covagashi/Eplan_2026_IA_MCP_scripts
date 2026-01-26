# RouteHints Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.RoutedConnection~RouteHints.html

---

Array of [Segment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment.html) by which this connection will be routed by routing algorithms.

Syntax

**C#**



public Segment[] RouteHints {get; set;}

public:

property array<Segment^>^ RouteHints {

   array<Segment^>^ get();

   void set (    array<Segment^>^ value);

}


#### Property Value

Returns array containing route hints or empty array.

Remarks

Can be set as `null` value. In this case it is treated as empty array.

Segments from `RouteHints` are used by routing algorithms as elements through which connection have to pass.
