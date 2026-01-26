# CreateChamferedRectangle(Project,Double,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateChamferedRectangle(Project,Double,Double,Double).html

---

Creates new chamfer rectangle drilling in project.

Syntax

**C#**



public void CreateChamferedRectangle( 

   Project pProject,

   double dWidth,

   double dHeight,

   double dChamferLength

)

public:

void CreateChamferedRectangle( 

   Project^ pProject,

   double dWidth,

   double dHeight,

   double dChamferLength

)


#### Parameters

*pProject*


*dWidth*
:   Width of the drilling. Must be greater than 0.

*dHeight*
:   Height of the drilling. Must be greater than 0.

*dChamferLength*
:   Length of the rectangle chamfer. Must be greater than 0 and smaller than half of the width and half of the height.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` is `null`. |
| [System.ArgumentException](#) | Thrown if size parameter isn't grater than 0 or value is invalid. |
