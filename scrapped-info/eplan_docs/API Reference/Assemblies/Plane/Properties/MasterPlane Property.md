# MasterPlane Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane~MasterPlane.html

---

Returns the master plane.

Syntax

**C#**



public Plane MasterPlane {get;}

public:

property Plane^ MasterPlane {

   Plane^ get();

}


#### Property Value

Returns plane object or `null` if does not exists.

Remarks

In P8 two planes which are parallel, have the same parent and their additional types are correlated can be paired. In this case one of plane is master and second is opposite. This property helps to get master plane from pair to which this plane belongs to.
