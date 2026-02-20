# Create(Page,Arc,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionCircle~Create(Page,Arc,PointD).html

---

Creates the DimensionCircle object.

Syntax

**C#**



public void Create( 

   Page page,

   Arc circle,

   PointD vertex

)

public:

void Create( 

   Page^ page,

   Arc^ circle,

   PointD vertex

)


#### Parameters

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where DimensionCircle will be placed on.

*circle*
:   [Arc](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Arc.html) where DimensionCircle will be created.

*vertex*
:   End point of DimensionCircle.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `circle` is `null`. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the Eplan::EplApi::DataModel::Graphics::Arc is not circle. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
