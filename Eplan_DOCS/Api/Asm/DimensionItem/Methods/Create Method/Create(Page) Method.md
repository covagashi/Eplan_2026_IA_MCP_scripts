# Create(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~Create(Page).html

---

Creates DimensionItem on a given page.

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
:   Page

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
