# AddArticleReference(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~AddArticleReference(String).html

---

Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Connection. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

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

ArticleReference added to the Connection

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when this Connection cannot have Articles |
| [System.ArgumentNullException](#) | Thrown when `strArticleName` is `null`. |
| [FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~IsFixedDevice.html) is true. |

Remarks

Stores the article from System article database in the Project. Adds one article with variant 1 and count 1. Adds the article to the Connection object only if the part already exists in the system or project database.
