# AddArticleReference(String,String,UInt32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser~AddArticleReference(String,String,UInt32).html

---

Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the IArticleUser. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

Syntax

**C#**



ArticleReference AddArticleReference( 

   string strArticleNR,

   string strVariantNR,

   uint nCount

)

ArticleReference^ AddArticleReference( 

   String^ strArticleNR,

   String^ strVariantNR,

   uint nCount

)


#### Parameters

*strArticleNR*
:   article's number

*strVariantNR*
:   article's variant number

*nCount*
:   count of articles to add

#### Return Value

Article added to the IArticleUser

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [System.ArgumentNullException](#) | Thrown when `strArticleNR` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strVariantNR` is `null`. |
| [CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | Thrown when it was impossible to get valid `property index`. |

Remarks

Stores the article from System article database in the Project
