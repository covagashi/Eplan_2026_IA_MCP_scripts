# CreateRectangle(Project,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRectangle(Project,Double,Double).html

---

Creates new rectangle drilling in project.

Syntax

**C#**



public void CreateRectangle( 

   Project pProject,

   double dWidth,

   double dHeight

)

public:

void CreateRectangle( 

   Project^ pProject,

   double dWidth,

   double dHeight

)


#### Parameters

*pProject*


*dWidth*
:   Width of the drilling. Must be greater than 0.

*dHeight*
:   Height of the drilling. Must be greater than 0.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` is `null`. |
| [System.ArgumentException](#) | Thrown if size parameter isn't grater than 0. |
