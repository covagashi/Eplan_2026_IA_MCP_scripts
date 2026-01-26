# ArticleReferences Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ArticleReferences.html

---

Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by Function.

Syntax

**C#**



public virtual ArticleReference[] ArticleReferences {get;}

public:

virtual property array<ArticleReference^>^ ArticleReferences {

   array<ArticleReference^>^ get();

}


#### Property Value

ArticleReferences related with the Function.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for Functions throws exception |

Remarks

The property does not work for Functions retrieved from transient objects, like macros. In this case please use properties FUNC\_ARTICLE\_PARTNR, FUNC\_ARTICLE\_VARIANT, FUNC\_ARTICLE\_COUNT
