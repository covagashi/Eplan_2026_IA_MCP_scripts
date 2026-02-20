# StartVertex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingSegment~StartVertex.html

---

Point in 3d space which is the beginning of routing segment.

Syntax

**C#**



public PointD3D StartVertex {get; set;}

public:

property PointD3D StartVertex {

   PointD3D get();

   void set (    PointD3D value);

}


Remarks

The coordinate value is relative to the parent. When setting it, also relative transformation could be adjusted.
