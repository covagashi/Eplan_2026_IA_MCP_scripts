# TopLevelParent Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~TopLevelParent.html

---

Gets the root 3d placement from tree of 3d elements which this object is part of.

Syntax

**C#**



public Placement3D TopLevelParent {get;}

public:

property Placement3D^ TopLevelParent {

   Placement3D^ get();

}


Remarks

Top level parent is being found by moving up in hierarchy of objects until a placement without a parent is found. In most case this will be layout space in which object is placed.
