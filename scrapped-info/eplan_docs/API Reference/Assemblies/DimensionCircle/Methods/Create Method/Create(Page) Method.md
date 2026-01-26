# Create(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionCircle~Create(Page).html

---

This method should never be used. Always throws NotImplementedException. DimensionCircle cannot be created without circle.

Syntax

**C#**



public void Create( 

   Page page

)

public:

void Create( 

   Page^ page

)


#### Parameters

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) the Circle will be placed on.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotImplementedException](#) | Always thrown. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
