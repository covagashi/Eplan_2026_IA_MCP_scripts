# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingAccessory~CreateTransient.html

---

Creates transient and not placed routing accessory object.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   double dDiameter

)

public:

void CreateTransient( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   double dDiameter

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*dDiameter*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the component cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
