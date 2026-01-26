# CreateContour(Project,String,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateContour(Project,String,List{Placement3D}).html

---

Creates a new drilling in the shape of the given contour.

Syntax

**C#**



public static Drilling CreateContour( 

   Project oProject,

   string strContureName,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Drilling^ CreateContour( 

   Project^ oProject,

   String^ strContureName,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*


*strContureName*
:   Full path with extension ("\*.fc1") to file containing a contour.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Drilling.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pInstallationSpace` or `strContureName` is `null` or empty. |
