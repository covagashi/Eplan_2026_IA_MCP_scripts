# IsMeshCreated Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~IsMeshCreated.html

---

Returns `true` if a mesh is created for this objects and assigned for it.

Syntax

**C#**



public bool IsMeshCreated {get;}

public:

property bool IsMeshCreated {

   bool get();

}


Remarks

Objects without a mesh represents a logical instance and no collision will be reported for them. To check if object collides then its parent or all its children which have mesh should be checked.
