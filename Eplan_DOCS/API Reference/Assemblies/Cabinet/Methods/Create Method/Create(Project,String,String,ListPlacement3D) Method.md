# Create(Project,String,String,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Cabinet~Create(Project,String,String,List{Placement3D}).html

---

Creates not placed Cabinet object.

Syntax

**C#**



public static Cabinet Create( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Cabinet^ Create( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Cabinet object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Cabinet cannot be created. |

Remarks

If strArticleVariant is null or empty, variant "1" is used.
