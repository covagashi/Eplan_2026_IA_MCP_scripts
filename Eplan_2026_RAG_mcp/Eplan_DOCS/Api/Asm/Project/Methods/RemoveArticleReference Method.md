# RemoveArticleReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~RemoveArticleReference.html

---

Removes the ArticleReference from the Project

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
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object in the articlereference is not this Project |

Remarks

The articlereference must belong to the Project.
