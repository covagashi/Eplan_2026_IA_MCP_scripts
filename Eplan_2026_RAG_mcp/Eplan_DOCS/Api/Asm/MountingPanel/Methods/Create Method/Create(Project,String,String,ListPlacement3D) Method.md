# Create(Project,String,String,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel~Create(Project,String,String,List{Placement3D}).html

---

Creates not placed MountingPanel object.

Syntax

**C#**



public static MountingPanel Create( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   List<Placement3D> listOfAdditionalPlacements

)

public:

static MountingPanel^ Create( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   List<Placement3D^>^ listOfAdditionalPlacements

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*listOfAdditionalPlacements*
:   additional created objects like holders and busbar objects

#### Return Value

The created MountingPanel object system.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingPanel cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
