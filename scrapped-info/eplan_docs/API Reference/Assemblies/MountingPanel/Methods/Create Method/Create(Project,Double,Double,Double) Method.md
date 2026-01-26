# Create(Project,Double,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel~Create(Project,Double,Double,Double).html

---

Creates not placed, article free MountingPanel object with given dimensions.

Syntax

**C#**



public void Create( 

   Project oProject,

   double dHeight,

   double dWidth,

   double dDepth

)

public:

void Create( 

   Project^ oProject,

   double dHeight,

   double dWidth,

   double dDepth

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*dHeight*
:   Height of the MountingPanel. Must be grater then zero.

*dWidth*
:   Length of the MountingPanel. Must be grater then zero.

*dDepth*
:   Depth of the MountingPanel. Must be grater then zero.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingPanel cannot be created. |
