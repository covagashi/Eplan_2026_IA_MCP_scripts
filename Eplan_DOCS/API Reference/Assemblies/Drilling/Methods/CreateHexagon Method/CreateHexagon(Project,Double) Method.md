# CreateHexagon(Project,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateHexagon(Project,Double).html

---

Creates new hexagon drilling in project.

Syntax

**C#**



public void CreateHexagon( 

   Project pProject,

   double dEdgeLength

)

public:

void CreateHexagon( 

   Project^ pProject,

   double dEdgeLength

)


#### Parameters

*pProject*


*dEdgeLength*
:   Length of one edge of the drilling. Must be greater than 0.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` is `null`. |
| [System.ArgumentException](#) | Thrown if edge length isn't greater than 0. |
