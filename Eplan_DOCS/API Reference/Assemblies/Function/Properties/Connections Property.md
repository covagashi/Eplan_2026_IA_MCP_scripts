# Connections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Connections.html

---

Returns [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s that have the Functions as a start function or end function.

Syntax

**C#**



public virtual Connection[] Connections {get;}

public:

virtual property array<Connection^>^ Connections {

   array<Connection^>^ get();

}


#### Property Value

the connections related with the Function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for connections throws exception |

Remarks

For [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html), method returns all [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s belonging to all representation types of this cable.
