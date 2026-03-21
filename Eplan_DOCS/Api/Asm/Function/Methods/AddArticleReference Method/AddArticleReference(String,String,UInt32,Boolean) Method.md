# AddArticleReference(String,String,UInt32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~AddArticleReference(String,String,UInt32,Boolean).html

---

Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Function.

Syntax

**C#**



public virtual ArticleReference AddArticleReference( 

   string strArticleNR,

   string strVariantNR,

   uint nCount,

   bool bClean

)

public:

virtual ArticleReference^ AddArticleReference( 

   String^ strArticleNR,

   String^ strVariantNR,

   uint nCount,

   bool bClean

)


#### Parameters

*strArticleNR*
:   article's number

*strVariantNR*
:   article's variant number

*nCount*
:   count of articles to add

*bClean*
:   Some ArticleReferences might not be completly cleaned in the past. Setting parameter to true allows to clean ArticleReference position before inserting new one.

#### Return Value

ArticleReference added to the Function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [System.ArgumentNullException](#) | Thrown when `strArticleNR` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strVariantNR` is `null`. |
| [CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | Thrown when it was impossible to add ArticleReference. This happens for example when 2nd ArticleReference is added to a 2D Function having ArticlePlacement category |

Remarks

Stores the article from System article database in the Project. Adds the article to the Function object only if the part already exists in the system or project database. Functions of category ArticlePlacement can have only 1 ArticleReference object. In such case, when a Function is additionally 2D, its counter is adjusted to "1" value.
