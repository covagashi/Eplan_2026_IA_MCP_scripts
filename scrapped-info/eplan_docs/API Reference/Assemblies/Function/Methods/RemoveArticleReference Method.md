# RemoveArticleReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~RemoveArticleReference.html

---

Removes the ArticleReference from the Function

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
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object in the articlereference is not this Function |
| [FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsFixedDevice.html) is true. |

Remarks

The articlereference must belong to the Function.
