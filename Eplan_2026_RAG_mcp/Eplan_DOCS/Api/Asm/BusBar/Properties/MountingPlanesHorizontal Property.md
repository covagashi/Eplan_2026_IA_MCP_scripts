# MountingPlanesHorizontal Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~MountingPlanesHorizontal.html

---

Array of mounting planes horizontal

Syntax

**C#**



public Tuple<Plane,Plane>[] MountingPlanesHorizontal {get;}

public:

property array<Tuple<Plane^,Plane^>^>^ MountingPlanesHorizontal {

   array<Tuple<Plane^,Plane^>^>^ get();

}


Remarks

Returns array planes as pairs (upper, lower)
