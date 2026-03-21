# BendingPoints Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~BendingPoints.html

---

Array of bending points.

Syntax

**C#**



public PointD3D[] BendingPoints {get; set;}

public:

property array<PointD3D>^ BendingPoints {

   array<PointD3D>^ get();

   void set (    array<PointD3D>^ value);

}


Remarks

Please be aware that the bending points are different than in GUI during the interaction  
In API the bending points coordinates are relative to local coordinates system There is also 1 extra point at each ending of the bus bar added by default. The property cannot be used to add or remove bending poins but only to change existing ones.
