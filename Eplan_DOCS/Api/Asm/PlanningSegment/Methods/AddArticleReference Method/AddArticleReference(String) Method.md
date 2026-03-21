# AddArticleReference(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddArticleReference(String).html

---

Adds a new [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the PlanningSegment. Returns the added [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

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

ArticleReference added to the PlanningSegment

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when this PlanningSegment cannot have Articles |
| [System.ArgumentNullException](#) | Thrown when `strArticleName` is `null`. |
| [Eplan.EplApi.DataModel.CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | Thrown when there is too many article reference or `IsArticleDataReadOnly` is true. |
| [Eplan.EplApi.DataModel.FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~IsFixedDevice.html) is true. |

Remarks

Stores the article from System article database in the Project Adds one article with variant 1 and count 1
