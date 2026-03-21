# Connections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Connections.html

---

Returns connections which start or end at this connection point.

Syntax

**C#**



public Connection[] Connections {get;}

public:

property array<Connection^>^ Connections {

   array<Connection^>^ get();

}


Remarks

Returns `NULL` if this Pin object has been obtained from a FunctionDefinition object.
