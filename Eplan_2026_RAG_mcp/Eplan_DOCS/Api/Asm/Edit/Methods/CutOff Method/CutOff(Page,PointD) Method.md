# CutOff(Page,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~CutOff(Page,PointD).html

---

Cut off objects at a given position and page.

Syntax

**C#**



public GraphicalPlacement[] CutOff( 

   Page oPage,

   PointD oPoint

)

public:

array<GraphicalPlacement^>^ CutOff( 

   Page^ oPage,

   PointD oPoint

)


#### Parameters

*oPage*
:   Page with object to cut off.

*oPoint*
:   Point of object to cut off.

#### Return Value

Modified graphical objects, empty array if it was last object, NULL if nothing was removed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
