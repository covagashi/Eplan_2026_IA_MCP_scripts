# Connection3D Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Connection3D.html

---

Returns the [Eplan.EplApi.DataModel.E3D.Connection3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D.html) which is a 3d representation of this connection.

Syntax

**C#**



public Connection3D Connection3D {get;}

public:

property Connection3D^ Connection3D {

   Connection3D^ get();

}


#### Property Value

3D representation of this connection or `null` if connectino doesn't have a 3d representation.
