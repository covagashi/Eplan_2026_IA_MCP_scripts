# FillingDegree Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingSegment~FillingDegree.html

---

The degree of routing segment filling in percent.

Syntax

**C#**



public double FillingDegree {get;}

public:

property double FillingDegree {

   double get();

}


Remarks

This is quotient of sum of connections/cables cross sections which are routed through this object and cross section of this routing segment.
