# TrackPotential Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~TrackPotential.html

---

Finds all connections which are in the same circuit as `oSourceConnection` and have the same potential.

Syntax

**C#**



public void TrackPotential( 

   Connection oSourceConnection,

   List<Connection> foundConnectionList

)

public:

void TrackPotential( 

   Connection^ oSourceConnection,

   List<Connection^>^ foundConnectionList

)


#### Parameters

*oSourceConnection*
:   Connection from which tracking potential is started.

*foundConnectionList*
:   List of connections that has the same potential as `oSourceConnection` and are in the same circuit.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if parameter `oSourceConnection` or `foundConnectionList` is `null` value. |
| [System.ArgumentException](#) | Throw if parameter `oSourceConnection` is invalid. |
