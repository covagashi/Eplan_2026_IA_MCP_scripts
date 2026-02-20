# TrackNet Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~TrackNet.html

---

Finds all connections in the same net as `oSourceConnection`.

Syntax

**C#**



public void TrackNet( 

   Connection oSourceConnection,

   List<Connection> foundConnectionList

)

public:

void TrackNet( 

   Connection^ oSourceConnection,

   List<Connection^>^ foundConnectionList

)


#### Parameters

*oSourceConnection*
:   Connection from which tracking net is started.

*foundConnectionList*
:   List of connections that are in the same net as `oSourceConnection`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if parameter `oSourceConnection` or `foundConnectionList` is `null` value. |
| [System.ArgumentException](#) | Throw if parameter `oSourceConnection` is invalid. |
