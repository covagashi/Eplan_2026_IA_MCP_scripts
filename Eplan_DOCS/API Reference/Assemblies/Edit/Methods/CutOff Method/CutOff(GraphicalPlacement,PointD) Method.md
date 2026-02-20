# CutOff(GraphicalPlacement,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~CutOff(GraphicalPlacement,PointD).html

---

Cut off given object at a given position. Page with object needs to be the currently opened page in graphical editor.

Syntax

**C#**



public GraphicalPlacement[] CutOff( 

   GraphicalPlacement oPlacement,

   PointD oPoint

)

public:

array<GraphicalPlacement^>^ CutOff( 

   GraphicalPlacement^ oPlacement,

   PointD oPoint

)


#### Parameters

*oPlacement*
:   Object to cut. Page with object needs to be the currently opened page in graphical editor.

*oPoint*
:   Point of object to cut off.

#### Return Value

Modified graphical objects, empty array if it was last object, NULL if nothing was removed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown when page with 'oPlacement' is not the currently opened page in graphical editor. |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
