# GetArticleReferencesWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetArticleReferencesWithCF.html

---

Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given filter.

Syntax

**C#**



public ArticleReference[] GetArticleReferencesWithCF( 

   ICustomFilter filter

)

public:

array<ArticleReference^>^ GetArticleReferencesWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given custom filter. \* All [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s if filter is `null`. \* Only valid ArticleReferences are returned (where ArticleReference.Count > 0 and ArticleReference.PartNr <> ""). \* This method doesn't return ArticleReference from ConnectionDefinitionPoint. ArticleReferences are transient objects - they are in fact on a corresponding Connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
