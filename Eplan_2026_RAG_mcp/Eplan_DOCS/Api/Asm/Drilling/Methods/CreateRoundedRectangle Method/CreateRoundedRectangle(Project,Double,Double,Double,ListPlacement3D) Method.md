# CreateRoundedRectangle(Project,Double,Double,Double,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic475.html

---

Creates new rounded rectangle drilling in project.

Syntax

**C#**



public static Drilling CreateRoundedRectangle( 

   Project oProject,

   double dWidth,

   double dHeight,

   double dDiameter,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Drilling^ CreateRoundedRectangle( 

   Project^ oProject,

   double dWidth,

   double dHeight,

   double dDiameter,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*


*dWidth*
:   Width of the drilling. Must be greater than 0.

*dHeight*
:   Height of the drilling. Must be greater than 0.

*dDiameter*
:   Diameter of the rectangle roundings. Must be greater than 0 and smaller than half of the width and half of the height.

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
