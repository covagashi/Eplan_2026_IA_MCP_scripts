# CreateTransient(Project,String,String,Double,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic492.html

---

Creates transient and not placed MountingRail object with given length.

Syntax

**C#**



public static MountingRail CreateTransient( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   double dLength,

   List<Placement3D> listOfAdditionalObjects

)

public:

static MountingRail^ CreateTransient( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

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

*dLength*
:   Length of the MountingRail. Must be grater then zero.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created MountingRail object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingRail cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
