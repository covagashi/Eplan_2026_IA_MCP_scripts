# CreateRoundedRectangle(Project,Double,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRoundedRectangle(Project,Double,Double,Double).html

---

Creates new rounded rectangle drilling in project.

Syntax

**C#**



public void CreateRoundedRectangle( 

   Project pProject,

   double dWidth,

   double dHeight,

   double dDiameter

)

public:

void CreateRoundedRectangle( 

   Project^ pProject,

   double dWidth,

   double dHeight,

   double dDiameter

)


#### Parameters

*pProject*


*dWidth*
:   Width of the drilling. Must be greater than 0.

*dHeight*
:   Height of the drilling. Must be greater than 0.

*dDiameter*
:   Diameter of the rectangle roundings. Must be greater than 0 and smaller than half of the width and half of the height.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` is `null`. |
| [System.ArgumentException](#) | Thrown if size parameter isn't grater than 0 or value is invalid. |
