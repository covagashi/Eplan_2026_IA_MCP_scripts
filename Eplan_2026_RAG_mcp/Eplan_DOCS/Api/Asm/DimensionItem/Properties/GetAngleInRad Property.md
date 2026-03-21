# GetAngleInRad Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~GetAngleInRad.html

---

Gets angle value in radians for angular dimension type only.

Syntax

**C#**



public double GetAngleInRad {get;}

public:

property double GetAngleInRad {

   double get();

}


Remarks

In case of DimensionItem type is different than angular, Double.NaN is returned.
