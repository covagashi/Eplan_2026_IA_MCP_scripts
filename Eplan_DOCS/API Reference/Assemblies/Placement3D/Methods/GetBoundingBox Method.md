# GetBoundingBox Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBox.html

---

Returns bounding box of a Placement3D.

Syntax

**C#**



public Rect3D GetBoundingBox( 

   bool bWithChildren

)

public:

Rect3D GetBoundingBox( 

   bool bWithChildren

)


#### Parameters

*bWithChildren*
:   If true, consider also children

Remarks

The method returns minimal bounding box which covers a Placement3D (Function3D, MountingPanel, Cabinet, etc) in absolute coordinates system. For example in case of InstallationSpace, when used with bWithChildren=true, it returns box which covers all placed Placements3D.
