# GetArticleReferences Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetArticleReferences.html

---

Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given filter.

Syntax

**C#**



public ArticleReference[] GetArticleReferences( 

   ArticleReferencesFilter filter

)

public:

array<ArticleReference^>^ GetArticleReferences( 

   ArticleReferencesFilter^ filter

)


#### Parameters

*filter*
:   a [ArticleReferencesFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencesFilter.html), can be `null`

#### Return Value

\* [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given [ArticleReferencesFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencesFilter.html). \* All [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s if filter is `null`. \* only valid ArticleReferences are returned (where ArticleReference.Count > 0 and ArticleReference.PartNr <> ""). \* method doesn't return ArticleReference from ConnectionDefinitionPoint. ArticleReferences are transient objects - they are in fact on a corresponding Connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
