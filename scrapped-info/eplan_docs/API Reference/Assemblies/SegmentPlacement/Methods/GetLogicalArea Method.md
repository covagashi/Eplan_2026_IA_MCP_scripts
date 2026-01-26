# GetLogicalArea Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement~GetLogicalArea.html

---

Returns a rectangle which is the logical area of the object derived from SymbolReference. For objects having symbols consisting of segments, this method returns the bounding box of the polyline created by those segments.

Syntax

**C#**



public override RectangleD GetLogicalArea()

public:

RectangleD GetLogicalArea(); override


Exceptions

| Exception | Description |
| --- | --- |
| [System.NotImplementedException](#) | Thrown when the object doesn't have a logical area. |

Remarks

Logical area is a region where something that belongs to the object represented by the symbol can be placed in. This term applies only to some special kinds of functions - those having resizable symbol that encompasses other symbols (e.g. macro box, location box, a cable's shielding, cable definition line).
