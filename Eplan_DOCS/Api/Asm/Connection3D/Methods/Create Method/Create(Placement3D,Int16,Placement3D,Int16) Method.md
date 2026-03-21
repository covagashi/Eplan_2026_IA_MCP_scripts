# Create(Placement3D,Int16,Placement3D,Int16) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D~Create(Placement3D,Int16,Placement3D,Int16).html

---

Creates connection between two 3d placements.

Syntax

**C#**



public void Create( 

   Placement3D pStartObject,

   short nStartIndex,

   Placement3D pEndObject,

   short nEndIndex

)

public:

void Create( 

   Placement3D^ pStartObject,

   short nStartIndex,

   Placement3D^ pEndObject,

   short nEndIndex

)


#### Parameters

*pStartObject*
:   [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) from which connection will start.

*nStartIndex*
:   Index of [Eplan.EplApi.DataModel.ConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition.html) will be the starting point of new connection.

*pEndObject*
:   [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) which will be connection end.

*nEndIndex*
:   Index of [Eplan.EplApi.DataModel.ConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition.html) will be the ending point of new connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when connection cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `pStartObject` parameter is `null`. |
| [System.ArgumentNullException](#) | Thrown when `pEndObject` parameter is `null`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when this object has already been created. |

Remarks

This method can create connection between connection points of two 3d functions. It also enables user not to specify connection point for one or both connection end. To do this index of value `-1` needs to be passed as index of connection point.

Example

**C#**

```
//connecting two 3d functions using connection points 

Connection3D oConnection3D = new Connection3D();

oConnection3D.Create(oFunction3D1, oFunction3D1.ConnectionPointPositions[0].Index, oFunction3D2, oFunction3D2.ConnectionPointPositions[2].Index);

//creating connection between two 3d function and only for one of them a connection point is specified

Connection3D oConnection3DOneConnectionPoint = new Connection3D();

oConnection3D.Create(oFunction3D1, oFunction3D1.ConnectionPointPositions[0].Index, oFunction3D2, -1);

```
