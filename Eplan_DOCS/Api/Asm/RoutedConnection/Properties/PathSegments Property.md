# PathSegments Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.RoutedConnection~PathSegments.html

---

Array of [Segment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment.html) by which this connection is passing through.

Syntax

**C#**



public Segment[] PathSegments {get; set;}

public:

property array<Segment^>^ PathSegments {

   array<Segment^>^ get();

   void set (    array<Segment^>^ value);

}


#### Property Value

Returns array containing path segments or empty array.

Remarks

Can be set as `null` value. This is treated as empty array.
