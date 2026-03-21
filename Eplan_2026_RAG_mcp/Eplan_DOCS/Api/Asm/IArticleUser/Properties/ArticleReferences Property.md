# ArticleReferences Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser~ArticleReferences.html

---

Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by IArticleUser.

Syntax

**C#**



ArticleReference[] ArticleReferences {get;}

property array<ArticleReference^>^ ArticleReferences {

   array<ArticleReference^>^ get();

}


#### Property Value

ArticleReferences related with the IArticleUser.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal error occures. For more information check message od exception. |
