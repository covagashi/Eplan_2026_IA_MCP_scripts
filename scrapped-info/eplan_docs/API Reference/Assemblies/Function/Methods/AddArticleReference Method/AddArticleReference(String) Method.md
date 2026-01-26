# AddArticleReference(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~AddArticleReference(String).html

---

Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Function. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

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

ArticleReference added to the Function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when this Function cannot have Articles |
| [System.ArgumentNullException](#) | Thrown when `strArticleName` is `null`. |
| [FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsFixedDevice.html) is true. |
| [CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | When 2nd ArticleReference is added to a 2D Function having ArticlePlacement category |

Remarks

Stores the article from System article database in a project. Adds one article with variant 1 and count 1. Adds the article to the Function object only if the part already exists in the system or project database. Functions of category ArticlePlacement can have only 1 ArticleReference object.
