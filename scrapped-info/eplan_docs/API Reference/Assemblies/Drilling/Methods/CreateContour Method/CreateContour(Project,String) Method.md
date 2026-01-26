# CreateContour(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateContour(Project,String).html

---

Creates a new drilling in the shape of the given contour.

Syntax

**C#**



public void CreateContour( 

   Project pProject,

   string strContureName

)

public:

void CreateContour( 

   Project^ pProject,

   String^ strContureName

)


#### Parameters

*pProject*


*strContureName*
:   Full path with extension ("\*.fc1") to file containing a contour.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` or `strContureName` is `null` or empty. |
