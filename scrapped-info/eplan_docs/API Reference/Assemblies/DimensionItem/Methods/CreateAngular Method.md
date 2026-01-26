# CreateAngular Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~CreateAngular.html

---

Creates an angular DimensionItem on the given page.

Syntax

**C#**



public void CreateAngular( 

   Page page,

   PointD pntFirstDimPoint,

   PointD pntSecondDimPoint,

   PointD pntEndDimPoint

)

public:

void CreateAngular( 

   Page^ page,

   PointD pntFirstDimPoint,

   PointD pntSecondDimPoint,

   PointD pntEndDimPoint

)


#### Parameters

*page*
:   Page

*pntFirstDimPoint*
:   First point of the DimensionItem.

*pntSecondDimPoint*
:   Second point of the DimensionItem.

*pntEndDimPoint*
:   End point of the DimensionItem.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when there are at least two identical points. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
