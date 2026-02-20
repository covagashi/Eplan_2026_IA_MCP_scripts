# Create(InstallationSpace,PointD3D[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingSpline~Create(InstallationSpace,PointD3D[]).html

---

Create new routing spline in P8 project.

Syntax

**C#**



public void Create( 

   InstallationSpace pInstallationSpace,

   PointD3D[] arrPointsOnSpline

)

public:

void Create( 

   InstallationSpace^ pInstallationSpace,

   array<PointD3D>^ arrPointsOnSpline

)


#### Parameters

*pInstallationSpace*
:   InstallationSpace object.

*arrPointsOnSpline*
:   List of [Eplan.EplApi.Base.PointD3D](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD3D.html), which are the nodes of the spline. At least 3 points needed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the RoutingSpline has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pInstallationSpace` is `null`, number of passed points on spline is less then three. |

Remarks

Method creates new routing spline and sets given installation space as its parent.
