# GetArticleReferencesWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetArticleReferencesWithFilterScheme.html

---

Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given filter from bill of materials-navigator.

Syntax

**C#**



public ArticleReference[] GetArticleReferencesWithFilterScheme( 

   string strFilterScheme

)

public:

array<ArticleReference^>^ GetArticleReferencesWithFilterScheme( 

   String^ strFilterScheme

)


#### Parameters

*strFilterScheme*
:   Scheme-name of filter in bill of materials-navigator

#### Return Value

\* [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given [ArticleReferencesFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencesFilter.html). \* If scheme-name is empty, the current filter scheme will be used. \* If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator. \* Only valid ArticleReferences are returned (where ArticleReference.Count > 0 and ArticleReference.PartNr <> ""). \* This method doesn't return ArticleReference from ConnectionDefinitionPoint. ArticleReferences are transient objects - they are in fact on a corresponding Connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |
