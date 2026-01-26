# Create(Placement3D,Placement3D) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D~Create(Placement3D,Placement3D).html

---

Creates connection between two 3d placements without specifying connection points.

Syntax

**C#**



public void Create( 

   Placement3D pStartObject,

   Placement3D pEndObject

)

public:

void Create( 

   Placement3D^ pStartObject,

   Placement3D^ pEndObject

)


#### Parameters

*pStartObject*
:   [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) from which connection will start.

*pEndObject*
:   [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) which will be connection end.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when connection cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `pStartObject` parameter is `null`. |
| [System.ArgumentNullException](#) | Thrown when `pEndObject` parameter is `null`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when this object has already been created. |

Example

**C#**

```


//creating 3d connection which exists between two 3d functions. Connection points are not specified

Connection3D oConnection3DNoConnectionPoints = new Connection3D();

oConnection3DNoConnectionPoints.Create(oFunction3D1, oFunction3D2);

```
