# CreateTransient(Project,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel~CreateTransient(Project,String,String).html

---

Creates transient and not placed MountingPanel object.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   string strArticleNr,

   string strVariant

)

public:

void CreateTransient( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingPanel cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
