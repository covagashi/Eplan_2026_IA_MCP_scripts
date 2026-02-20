# OppositePlane Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane~OppositePlane.html

---

Returns the opposite plane.

Syntax

**C#**



public Plane OppositePlane {get;}

public:

property Plane^ OppositePlane {

   Plane^ get();

}


#### Property Value

Returns plane object or `null` if does not exists.

Remarks

In P8 two planes which are parallel, have the same parent and their additional types are correlated can be paired. In this case one of plane is master and second is opposite. This property helps to get opposite plane from pair to which this plane belongs to.
