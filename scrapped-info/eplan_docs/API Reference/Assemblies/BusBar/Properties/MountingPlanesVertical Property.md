# MountingPlanesVertical Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~MountingPlanesVertical.html

---

Array of mounting planes vertical

Syntax

**C#**



public Tuple<Plane,Plane>[] MountingPlanesVertical {get;}

public:

property array<Tuple<Plane^,Plane^>^>^ MountingPlanesVertical {

   array<Tuple<Plane^,Plane^>^>^ get();

}


Remarks

Returns array planes as pairs (left, right)
