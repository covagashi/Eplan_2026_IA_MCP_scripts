# GetBoundingBox Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~GetBoundingBox.html

---

Returns the bounding box of the macro. This is the size and position of the macrobox.

Syntax

**C#**



public PointD[] GetBoundingBox()

public:

array<PointD>^ GetBoundingBox();


#### Return Value

the upperleft and the lowerright point of the box. Zero if nothing was found. this are absolute coordinates.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not opened before or could not opened successfully. |

Remarks

If the WindowMacro includes no macro box, both returned points will be (0,0).
