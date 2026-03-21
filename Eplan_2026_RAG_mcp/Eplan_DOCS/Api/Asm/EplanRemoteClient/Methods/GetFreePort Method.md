# GetFreePort Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~GetFreePort.html

---

Returns first free port which can act as a tunnel for remote server.

Syntax

**C#**



public static bool GetFreePort( 

   ref int nPort

)

public:

static bool GetFreePort( 

   int% nPort

)


#### Parameters

*nPort*
:   Port number

#### Return Value

Returns 0 if free tcp port was not found. Tcp port between MIN\_PORT\_NR (57315) and MAX\_PORT\_NR(65535) otherwise.
