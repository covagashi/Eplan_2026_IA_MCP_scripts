# GetBoundingBox3D Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~GetBoundingBox3D.html

---

Returns the least bounding box containing all 3d elements of macro in current variant.

Syntax

**C#**



public Rect3D GetBoundingBox3D()

public:

Rect3D GetBoundingBox3D();


#### Return Value

The least bounding box containing all 3d elements of macro in current variant.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not opened before or could not opened successfully. |

Remarks

Position of bounding box is relative to coordinate system of macro.

If the WindowMacro doesn't contain any 3d object in current variant then bounding box has dimensions 0.
