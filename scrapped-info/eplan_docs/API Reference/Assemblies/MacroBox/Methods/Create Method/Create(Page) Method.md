# Create(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~Create(Page).html

---

Creates a MacroBox object.

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
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a MacroBox cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown if the default macro box symbol ('SPECIAL/MC(44)') is not available. |
