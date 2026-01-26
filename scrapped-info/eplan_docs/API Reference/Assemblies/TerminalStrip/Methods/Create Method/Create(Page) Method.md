# Create(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~Create(Page).html

---

Creates a TerminalStrip object placed on a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) given as a parameter.

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
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where the TerminalStrip will be located on.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if the TerminalStrip cannot be created. |
| [System.ArgumentNullException](#) | Thrown if `page` parameter is `NULL`. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown if the `page` parameter has its PageType set to the wrong document type. |
