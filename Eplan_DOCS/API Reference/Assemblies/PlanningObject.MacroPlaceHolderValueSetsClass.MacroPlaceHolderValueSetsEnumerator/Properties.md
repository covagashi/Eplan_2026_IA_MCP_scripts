# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic756.html

---

Adds a new [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the PlanningSegment.

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

Article added to the PlanningSegment

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [System.ArgumentNullException](#) | Thrown when `strArticleNR` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strVariantNR` is `null`. |
| [Eplan.EplApi.DataModel.CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | Thrown when there is too many article reference or `IsArticleDataReadOnly` is true. |
| [Eplan.EplApi.DataModel.FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~IsFixedDevice.html) is true. |

Remarks

Stores the article from System article database in the Project
