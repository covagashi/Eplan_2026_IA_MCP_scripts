# Create(Project,String,String,Int32,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBarSystem~Create(Project,String,String,Int32,Double).html

---

Creates not placed Busbar system.

Syntax

**C#**



public void Create( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   int numberOfHolder,

   double dLength

)

public:

void Create( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   int numberOfHolder,

   double dLength

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*numberOfHolder*
:   number of holder.

*dLength*
:   length of busbar system.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the component cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
