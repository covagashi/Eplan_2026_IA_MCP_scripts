# AddArticleReference(String,String,UInt32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddArticleReference(String,String,UInt32,Boolean).html

---

Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Project. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

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

ArticleReference added to the Project

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the ArticleReference cannot be added |
| [System.ArgumentNullException](#) | Thrown when `strArticleNR` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strVariantNR` is `null`. |
| [CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | Thrown when it was impossible to get valid `property index`. |

Remarks

This method adds the article to the Project only if the part already exists in the system database.
