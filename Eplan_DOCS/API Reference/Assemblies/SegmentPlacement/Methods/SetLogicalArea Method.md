# SetLogicalArea Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement~SetLogicalArea.html

---

Sets rectangular logical area for objects derived from SymbolReference.

Syntax

**C#**



public override void SetLogicalArea( 

   PointD oPoint1,

   PointD oPoint2

)

public:

void SetLogicalArea( 

   PointD oPoint1,

   PointD oPoint2

) override


#### Parameters

*oPoint1*
:   First of the two points defining a rectangular logical area on the page.

*oPoint2*
:   Second of the two points defining a rectangular logical area on the page.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotImplementedException](#) | Thrown when the method is not implemented for specific kind of function |

Remarks

Logical area is a region where something that belongs to the object represented by the symbol can be placed in. This term applies only to some special kinds of functions - those having resizable symbol that encompasses other symbols (e.g. macro box, location box, a cable's shielding, cable definition line). Note: After setting the logical area with this method the [Eplan.EplApi.DataModel.SymbolReference.LogicalAreaSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~LogicalAreaSegments.html) property returns an array containing 3 segments (that represent a rectangular area) Please remember that while changing LocationArea of shielding, symbol variant may be also changed. If original symbol variant number is 0 or 2 (horizontal) new variant number is set by comparing sign of old and new logical area offsets (Offset X = pEnd.X - pStart.X). If offset sign changed, symbol variant number is changed from 0 is 2 and vice versa. Analogically, if original symbol variant number is 1 or 3 (vertical) new variant number is set by comparing Y offsets and the variant number is changed or not.
