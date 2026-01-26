# AddArticleReference(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddArticleReference(String).html

---

Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Project. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

Syntax

**C#**



public virtual ArticleReference AddArticleReference( 

   string strArticleNR

)

public:

virtual ArticleReference^ AddArticleReference( 

   String^ strArticleNR

)


#### Parameters

*strArticleNR*
:   number of added article

#### Return Value

ArticleReference added to the Project

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the ArticleReference cannot be added |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when this Project cannot have more ArticleReferences |
| [System.ArgumentNullException](#) | Thrown when `strArticleName` is `null`. |

Remarks

Stores the article from System article database in the Project. Adds one article with variant 1 and count 1. This method adds the article to the Project only if the part already exists in the system database.
