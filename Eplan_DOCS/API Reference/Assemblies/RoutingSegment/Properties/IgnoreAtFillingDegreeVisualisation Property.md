# IgnoreAtFillingDegreeVisualisation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingSegment~IgnoreAtFillingDegreeVisualisation.html

---

If true, then this routing segment is ignored while calculating any filling degree in P8 project.

Syntax

**C#**



public bool IgnoreAtFillingDegreeVisualisation {get; set;}

public:

property bool IgnoreAtFillingDegreeVisualisation {

   bool get();

   void set (    bool value);

}


Remarks

Property `FillingDegree` also isn't calculeted automaticly.
