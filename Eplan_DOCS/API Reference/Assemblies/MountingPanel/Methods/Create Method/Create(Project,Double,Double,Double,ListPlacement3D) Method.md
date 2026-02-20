# Create(Project,Double,Double,Double,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic487.html

---

Creates not placed, article free MountingPanel object with given dimensions.

Syntax

**C#**



public static MountingPanel Create( 

   Project oProject,

   double dHeight,

   double dWidth,

   double dDepth,

   List<Placement3D> listOfAdditionalPlacements

)

public:

static MountingPanel^ Create( 

   Project^ oProject,

   double dHeight,

   double dWidth,

   double dDepth,

   List<Placement3D^>^ listOfAdditionalPlacements

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*dHeight*


*dWidth*
:   Length of the MountingPanel. Must be grater then zero.

*dDepth*


*listOfAdditionalPlacements*
:   additional created objects like holders and busbar objects

#### Return Value

The created MountingPanel object system.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingPanel cannot be created. |
