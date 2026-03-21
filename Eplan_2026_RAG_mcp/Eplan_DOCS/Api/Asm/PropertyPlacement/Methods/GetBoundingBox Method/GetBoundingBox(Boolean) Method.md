# GetBoundingBox(Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement~GetBoundingBox(Boolean).html

---

PropertyPlacement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size.

Syntax

**C#**



public virtual PointD[] GetBoundingBox( 

   bool relative

)

public:

virtual array<PointD>^ GetBoundingBox( 

   bool relative

)


#### Parameters

*relative*
:   If set to false absolute bounding box points will be returned.

#### Return Value

Two points are always returned. First one is a lower-left corner and second is upper-right corner of the bounding box.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when something went wrong in internal function. |
| [System.InvalidOperationException](#) | Thrown when bounding box cannot be calculated. |
