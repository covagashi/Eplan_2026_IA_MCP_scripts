# CreateTransient(Project,Double,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel~CreateTransient(Project,Double,Double,Double).html

---

Creates not placed, article free MountingPanel object with given dimensions.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   double dHeight,

   double dWidth,

   double dDepth

)

public:

void CreateTransient( 

   Project^ oProject,

   double dHeight,

   double dWidth,

   double dDepth

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*dHeight*


*dWidth*
:   Length of the MountingPanel. Must be grater then zero.

*dDepth*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingPanel cannot be created. |
