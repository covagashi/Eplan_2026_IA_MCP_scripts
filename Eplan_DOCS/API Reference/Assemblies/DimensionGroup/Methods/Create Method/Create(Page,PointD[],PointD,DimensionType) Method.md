# Create(Page,PointD[],PointD,DimensionType) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DimensionGroup~Create(Page,PointD[],PointD,DimensionType).html

---

Creates DimensionGroup on a given page.

Syntax

**C#**



public void Create( 

   Page page,

   PointD[] dimensionPositions,

   PointD pntLocDimLine,

   DimensionGroup.Enums.DimensionType dimensionType

)

public:

void Create( 

   Page^ page,

   array<PointD>^ dimensionPositions,

   PointD pntLocDimLine,

   DimensionGroup.Enums.DimensionType dimensionType

)


#### Parameters

*page*
:   Page

*dimensionPositions*
:   Points of DimensionGroup.

*pntLocDimLine*
:   Point of DimensionGroup.

*dimensionType*
:   Type of DimensionGroup.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
