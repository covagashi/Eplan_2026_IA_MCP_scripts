# GetBoundingBoxRelative Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBoxRelative.html

---

Returns relative bounding box of a Placement3D.

Syntax

**C#**



public Rect3D GetBoundingBoxRelative()

public:

Rect3D GetBoundingBoxRelative();


Remarks

The method returns minimal bounding box which covers a Placement3D (Function3D, MountingPanel, Cabinet, etc) in relative coordinates system.
