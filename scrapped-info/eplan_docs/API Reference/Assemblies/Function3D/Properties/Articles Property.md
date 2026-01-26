# Articles Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~Articles.html

---

Returns [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s that are referenced by Function3D, and only those that are stored in project database.

Syntax

**C#**



public virtual Article[] Articles {get;}

public:

virtual property array<Article^>^ Articles {

   array<Article^>^ get();

}


#### Property Value

Articles related with the Function3D

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for Functions3D throws exception |

Remarks

This function returns only articles which are stored in the project. Although function might contain reference to Article (which resists in system database), so in this case following Properties need to be used: FUNC\_ARTICLE\_PARTNR, FUNC\_ARTICLE\_VARIANT, FUNC\_ARTICLE\_COUNT etc.
