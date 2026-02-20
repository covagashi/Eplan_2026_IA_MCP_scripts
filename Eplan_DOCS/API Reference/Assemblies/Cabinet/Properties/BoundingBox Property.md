# BoundingBox Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Cabinet~BoundingBox.html

---

Returns bounding box of this Cabinet.

Syntax

**C#**



public Rect3D BoundingBox {get;}

public:

property Rect3D BoundingBox {

   Rect3D get();

}


Remarks

Returns bounding box created by merging bounding boxes of its child items (recursively).
