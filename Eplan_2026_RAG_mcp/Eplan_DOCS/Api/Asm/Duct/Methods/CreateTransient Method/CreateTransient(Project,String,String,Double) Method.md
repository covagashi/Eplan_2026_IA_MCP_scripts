# CreateTransient(Project,String,String,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Duct~CreateTransient(Project,String,String,Double).html

---

Creates transient and not placed Duct object with given length.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   double dLength

)

public:

void CreateTransient( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   double dLength

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*dLength*
:   Length of duct. Must be grater then zero.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the duct cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
