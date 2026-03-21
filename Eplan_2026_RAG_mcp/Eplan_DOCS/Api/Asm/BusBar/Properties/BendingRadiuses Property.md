# BendingRadiuses Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~BendingRadiuses.html

---

Array of Bending Radiuses.

Syntax

**C#**



public double[] BendingRadiuses {get; set;}

public:

property array<double>^ BendingRadiuses {

   array<double>^ get();

   void set (    array<double>^ value);

}


Remarks

Please be aware that there is also 1 extra radius at each ending of the bus bar added by default.
