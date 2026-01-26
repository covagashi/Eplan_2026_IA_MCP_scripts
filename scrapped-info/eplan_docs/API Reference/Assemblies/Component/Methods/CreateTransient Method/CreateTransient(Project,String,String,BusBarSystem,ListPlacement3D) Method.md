# CreateTransient(Project,String,String,BusBarSystem,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic471.html

---

Creates not placed Component object.

Syntax

**C#**



public static Component CreateTransient( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   BusBarSystem __unnamed003,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Component^ CreateTransient( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   BusBarSystem^ __unnamed003,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*\_\_unnamed003*


*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Component.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the component cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
