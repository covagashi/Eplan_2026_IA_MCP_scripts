# Article Constructor(Project,String,String)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~_ctor(Project,String,String).html

---

Constructor. Creates a Article in Project with the specified strPartnr and strVariant.

Syntax

**C#**



public Article( 

   Project proj,

   string strPartnr,

   string strVariant

)

public:

Article( 

   Project^ proj,

   String^ strPartnr,

   String^ strVariant

)


#### Parameters

*proj*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the Function will be located in

*strPartnr*
:   this is the article number

*strVariant*
:   this is the article Variant

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `proj` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strPartnr` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strVariant` is `null`. |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [System.ArgumentException](#) | Thrown when `strPartNr` with `strVariant` already exists in the project. |
