# CreateHexagonTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateHexagonTransient.html

---

Creates new transient hexagon drilling.

Syntax

**C#**



public static Drilling CreateHexagonTransient( 

   Project oProject,

   double dEdgeLength,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Drilling^ CreateHexagonTransient( 

   Project^ oProject,

   double dEdgeLength,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*


*dEdgeLength*
:   Length of one edge of the drilling. Must be greater than 0.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Drilling.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pInstallationSpace` is `null`. |
| [System.ArgumentException](#) | Thrown if edge length isn't greater than 0. |
