# CutOff(PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~CutOff(PointD).html

---

Cut off objects at a given position, from page currently opened in graphical editor.

Syntax

**C#**



public GraphicalPlacement[] CutOff( 

   PointD oPoint

)

public:

array<GraphicalPlacement^>^ CutOff( 

   PointD oPoint

)


#### Parameters

*oPoint*
:   Point of object to cut off.

#### Return Value

Modified graphical objects, empty array if it was last object, NULL if nothing was removed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown when there is no page currently opened in graphical editor. |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
