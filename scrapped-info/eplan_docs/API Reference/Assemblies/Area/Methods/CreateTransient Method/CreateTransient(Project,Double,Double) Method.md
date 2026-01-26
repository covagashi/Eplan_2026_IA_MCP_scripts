# CreateTransient(Project,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Area~CreateTransient(Project,Double,Double).html

---

Creates transient not placed Area object.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   double x,

   double y

)

public:

void CreateTransient( 

   Project^ oProject,

   double x,

   double y

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*x*
:   Width of Area object.

*y*
:   Height of Area object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Area cannot be created. |
