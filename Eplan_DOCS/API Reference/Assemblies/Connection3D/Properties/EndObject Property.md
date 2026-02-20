# EndObject Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D~EndObject.html

---

Returns the second of two [Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s connected by this connection3D.

Syntax

**C#**



public Function3D EndObject {get;}

public:

property Function3D^ EndObject {

   Function3D^ get();

}


#### Property Value

- the second of two [Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s connected by this connection,
- `null` when there is no Function3D on this end of the connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the Function3D from project. |

Remarks

Name of 3d object can be different from value property of CONNECTION\_SOURCE or CONNECTION\_DESTINATION. If this connection is generated based on regular connection then those properties represents names of 2D source/target.
