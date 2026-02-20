# GetBoundingBox Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart~GetBoundingBox.html

---

Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size.

Syntax

**C#**



public override PointD[] GetBoundingBox()

public:

array<PointD>^ GetBoundingBox(); override


#### Return Value

Two points are always returned. First one is a lower-left corner and second is upper-right corner of bounding box.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when something went wrong in internal function. |
| [System.InvalidOperationException](#) | Thrown when bounding box cannot be calculated. |

Remarks

In order to use function `GetBoundingBox` property [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) can't be null.
