# PlaceAt Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PlaceAt.html

---

Places the segment onto the given page, in the given location.

Syntax

**C#**



public SymbolReference PlaceAt( 

   Page oPage,

   PointD pntLocation

)

public:

SymbolReference^ PlaceAt( 

   Page^ oPage,

   PointD pntLocation

)


#### Parameters

*oPage*
:   A page on which segment will be inserted.

*pntLocation*
:   Insertion point of the symbol being inserted.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when page is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when object cannot be created. |
