# CreateTapHoleTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateTapHoleTransient.html

---

Creates new tap hole in project.

Syntax

**C#**



public static Drilling CreateTapHoleTransient( 

   Project oProject,

   double dDiameter,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Drilling^ CreateTapHoleTransient( 

   Project^ oProject,

   double dDiameter,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*


*dDiameter*
:   Diameter of the tap hole. Must be greater than 0.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Drilling.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pInstallationSpace` is `null`. |
| [System.ArgumentException](#) | Thrown if parameter `dDiameter` isn't grater than 0. |
