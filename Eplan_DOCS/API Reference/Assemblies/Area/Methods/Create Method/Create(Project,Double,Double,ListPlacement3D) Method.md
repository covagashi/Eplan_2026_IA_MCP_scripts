# Create(Project,Double,Double,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Area~Create(Project,Double,Double,List{Placement3D}).html

---

Creates not placed Area object.

Syntax

**C#**



public static Area Create( 

   Project oProject,

   double x,

   double y,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Area^ Create( 

   Project^ oProject,

   double x,

   double y,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*x*
:   Width of Area object.

*y*
:   Height of Area object.

*listOfAdditionalObjects*
:   List of 3d objects additionaly created while Area object had been created.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Area cannot be created. |
