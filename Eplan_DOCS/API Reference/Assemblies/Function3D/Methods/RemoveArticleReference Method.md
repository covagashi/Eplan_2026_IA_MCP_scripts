# RemoveArticleReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~RemoveArticleReference.html

---

Removes the ArticleReference from the Function.

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
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object in the articlereference is not from this Function3D. |
| [Eplan.EplApi.DataModel.FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if **Eplan.EplApi.DataModel.E3D.Function3D.get\_IsFixedDevice** is true. |

Remarks

The articlereference must belong to the Function3D.
