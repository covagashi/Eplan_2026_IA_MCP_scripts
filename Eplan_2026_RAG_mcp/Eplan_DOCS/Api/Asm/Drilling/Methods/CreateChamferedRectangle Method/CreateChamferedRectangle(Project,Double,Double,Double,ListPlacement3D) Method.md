# CreateChamferedRectangle(Project,Double,Double,Double,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic474.html

---

Creates new chamfer rectangle drilling in project.

Syntax

**C#**



public static Drilling CreateChamferedRectangle( 

   Project oProject,

   double dWidth,

   double dHeight,

   double dChamferLength,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Drilling^ CreateChamferedRectangle( 

   Project^ oProject,

   double dWidth,

   double dHeight,

   double dChamferLength,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*


*dWidth*
:   Width of the drilling. Must be greater than 0.

*dHeight*
:   Height of the drilling. Must be greater than 0.

*dChamferLength*
:   Length of the rectangle chamfer. Must be greater than 0 and smaller than half of the width and half of the height.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Drilling.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pInstallationSpace` is `null`. |
| [System.ArgumentException](#) | Thrown if size parameter isn't grater than 0 or value is invalid. |
