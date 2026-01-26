# AddArticleReference(ArticleReference,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic111.html

---

Adds [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the ConnectionDefinitionPoint.

Syntax

**C#**



public ArticleReference AddArticleReference( 

   ArticleReference oArticle,

   bool bClean

)

public:

ArticleReference^ AddArticleReference( 

   ArticleReference^ oArticle,

   bool bClean

)


#### Parameters

*oArticle*
:   [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) object is a prototype for ArticleReference added to ConnectionDefinitionPoint.

*bClean*
:   Some ArticleReferences might not be completly cleaned in the past. Setting parameter to true allows to clean ArticleReference position before inserting new one.

#### Return Value

Article reference added to the ConnectionDefinitionPoint. Article reference passed as parameter is not changed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [System.ArgumentNullException](#) | Thrown when article number is `null`. |
| [System.ArgumentNullException](#) | Thrown when article variant is `null`. |
| [CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | Thrown when it was impossible to get valid `property index`. |
