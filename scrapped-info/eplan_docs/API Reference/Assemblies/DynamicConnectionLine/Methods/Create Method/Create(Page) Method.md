# Create(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DynamicConnectionLine~Create(Page).html

---

Creates DynamicConnectionLine object.

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
:   [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) inside which the object will be located.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a DynamicConnectionLine cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
