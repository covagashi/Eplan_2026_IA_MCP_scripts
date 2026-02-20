# CreateSlot(Project,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateSlot(Project,Double,Double).html

---

Creates new slot drilling in project.

Syntax

**C#**



public void CreateSlot( 

   Project pProject,

   double dWidth,

   double dHeight

)

public:

void CreateSlot( 

   Project^ pProject,

   double dWidth,

   double dHeight

)


#### Parameters

*pProject*


*dWidth*
:   Width of the drilling. Must be greater than `dHeight`.

*dHeight*
:   Height of the drilling. Must be greater than 0.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` is `null`. |
| [System.ArgumentException](#) | Thrown if any size parameter is incorrect. |
