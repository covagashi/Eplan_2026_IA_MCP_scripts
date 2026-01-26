# MakeConnectionExternalOrInternal Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~MakeConnectionExternalOrInternal.html

---

Forces one of the terminal's connections to be treated as internal or external connection. The connection passed by the 'pConn' parameter must be connected to the terminal (must be one of its connections).

Syntax

**C#**



public void MakeConnectionExternalOrInternal( 

   Connection pConn,

   Terminal.ConnectionSide side

)

public:

void MakeConnectionExternalOrInternal( 

   Connection^ pConn,

   Terminal.ConnectionSide side

)


#### Parameters

*pConn*


*side*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when the connection passed by the 'pConn' parameter is none of the terminal's connections. |
| [System.NotImplementedException](#) | Thrown when implementation of a requested interface isn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal functionality fails. |

Remarks

This information is stored as the terminal's property, not connection's. This means that after disconnecting an internal connection and connecting another connection to the same pin (connection point), the new one will also be internal.
