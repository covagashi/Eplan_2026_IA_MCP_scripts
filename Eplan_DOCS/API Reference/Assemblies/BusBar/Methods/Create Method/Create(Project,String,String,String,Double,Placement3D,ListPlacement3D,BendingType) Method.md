# Create(Project,String,String,String,Double,Placement3D,List<Placement3D>,BendingType) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic465.html

---

Creates unplaced bended bus bar object with given bending radius and form.

Syntax

**C#**



public static BusBar Create( 

   Project project,

   string partNr,

   string partVariant,

   string formFile,

   double bendingRadius,

   Placement3D copperBundle,

   List<Placement3D> listOfAdditionalObjects,

   BusBar.Enums.BendingType bendingType

)

public:

static BusBar^ Create( 

   Project^ project,

   String^ partNr,

   String^ partVariant,

   String^ formFile,

   double bendingRadius,

   Placement3D^ copperBundle,

   List<Placement3D^>^ listOfAdditionalObjects,

   BusBar.Enums.BendingType bendingType

)


#### Parameters

*project*
:   Project were the object will be created. Can't be null.

*partNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*partVariant*
:   Part variant of article.

*formFile*
:   Full path with extension ("\*.fp1") to a form file. Can't be null nor empty.

*bendingRadius*
:   Bending radius. Must be greater then zero.

*copperBundle*
:   Copper bundle as parent of bended bus.

*listOfAdditionalObjects*


*bendingType*
:   Bending type (0- flat, 1- edgewise)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the duct cannot be created. |

Remarks

If partVariant is null or have zero length default variant "1" is used. If copperBundle is null new copper bundle will be created.
