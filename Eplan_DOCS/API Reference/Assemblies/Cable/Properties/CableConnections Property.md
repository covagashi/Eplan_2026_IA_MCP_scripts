# CableConnections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable~CableConnections.html

---

Returns an array of Connection objects that exist under the cable definition line represented by this Cable object.

Syntax

**C#**



public Connection[] CableConnections {get;}

public:

property array<Connection^>^ CableConnections {

   array<Connection^>^ get();

}


Remarks

To associate a Cable with its Connections, Name and VisibleName should be set the same in Cable as in ConnectionDefinitionPoints.
