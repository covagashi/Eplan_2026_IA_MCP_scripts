# CreateRound(Project,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRound(Project,Double).html

---

Creates new round drilling in project.

Syntax

**C#**



public void CreateRound( 

   Project pProject,

   double dDiameter

)

public:

void CreateRound( 

   Project^ pProject,

   double dDiameter

)


#### Parameters

*pProject*


*dDiameter*
:   Diameter of the drilling. Must be greater than 0.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` is `null`. |
| [System.ArgumentException](#) | Thrown if parameter `dDiameter` isn't grater than 0. |
