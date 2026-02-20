# CreateMergedConnections Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~CreateMergedConnections.html

---

Returns an array of MergedConnection objects created from the connections passed in the array parameter. connections that belong to representing the same corresponding connections with different placement types are merged together into one merged connection in the output vector.

Syntax

**C#**



public static MergedConnection[] CreateMergedConnections( 

   Connection[] connections

)

public:

static array<MergedConnection^>^ CreateMergedConnections( 

   array<Connection^>^ connections

)


#### Parameters

*connections*

#### Return Value

An array of merged connections for the given connections.
