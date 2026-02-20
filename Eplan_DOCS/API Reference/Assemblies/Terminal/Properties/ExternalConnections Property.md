# ExternalConnections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~ExternalConnections.html

---

Array of [Terminal.ConnectionInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+ConnectionInfo.html) representing connections assigned to this `Terminal` which are connected over external connection points. None of those connections are bridge connections.

Syntax

**C#**



public Terminal.ConnectionInfo[] ExternalConnections {get;}

public:

property array<Terminal.ConnectionInfo^>^ ExternalConnections {

   array<Terminal.ConnectionInfo^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when interface cannot be initialized or it cannot return functions. |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal function fails. |
