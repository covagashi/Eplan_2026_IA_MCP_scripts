# RemoveArticleReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemoveArticleReference.html

---

Removes the ArticleReference from the PlanningSegment

Syntax

**C#**



public virtual void RemoveArticleReference( 

   ArticleReference artRef

)

public:

virtual void RemoveArticleReference( 

   ArticleReference^ artRef

)


#### Parameters

*artRef*
:   The articlereference to remove

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `artRef` is `null`. |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object in the articlereference is not this PlanningSegment |
| [Eplan.EplApi.DataModel.RemoveFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.RemoveFailedException.html) | Thrown when `IsArticleDataReadOnly` is true. |
| [Eplan.EplApi.DataModel.FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~IsFixedDevice.html) is true. |

Remarks

The articlereference must belong to the PlanningSegment.
