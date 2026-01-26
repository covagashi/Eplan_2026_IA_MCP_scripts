# UnGroup(Placement3D,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~UnGroup(Placement3D,Boolean,Boolean).html

---

Removes [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) only from the 3D group.

Syntax

**C#**



public void UnGroup( 

   Placement3D placement3D,

   bool removeEmptyGroup3D,

   bool redraw

)

public:

void UnGroup( 

   Placement3D^ placement3D,

   bool removeEmptyGroup3D,

   bool redraw

)


#### Parameters

*placement3D*
:   3D placement removed from the 3D group.

*removeEmptyGroup3D*
:   If true, the method will remove also the Group3D object when it becomes empty.

*redraw*
:   If true, GED is redrawn after the ungrouping.
