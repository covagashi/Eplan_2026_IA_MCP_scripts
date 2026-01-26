# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBarSystem~CreateTransient.html

---

Creates not placed transient Busbar system.

Syntax

**C#**



public static BusBarSystem CreateTransient( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   int numberOfHolder,

   double dLength,

   List<Placement3D> listOfAdditionalObjects

)

public:

static BusBarSystem^ CreateTransient( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   int numberOfHolder,

   double dLength,

   List<Placement3D^>^ listOfAdditionalObjects

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

*listOfAdditionalObjects*
:   additional created objects like holders and busbar objects. may be null

#### Return Value

The Busbar system.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the component cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
