# Create(PlugStrip,Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug~Create(PlugStrip,Page).html

---

Creates a Plug object related to a [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) given as a parameter. The plug's function definition will be chosen based on the plug strip's function definition:

- for "Male and female" plug strips, the plug will get "Male and Female pin" function definition,

- for "Male" plug strips, the plug will get "Male pin, 2 connection points" function definition,

- for "Female" plug strips, the plug will get "Female pin, 2 connection points" function definition

Syntax

**C#**



public void Create( 

   PlugStrip ps,

   Page page

)

public:

void Create( 

   PlugStrip^ ps,

   Page^ page

)


#### Parameters

*ps*
:   A [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) where the plug will be located.

*page*
:   A [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where the plug will be placed. If the page parameter is NULL, the plug will be un-placed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the plug cannot be created. |
| [System.ArgumentNullException](#) | Thrown when the `ps` parameters is `null`. |
