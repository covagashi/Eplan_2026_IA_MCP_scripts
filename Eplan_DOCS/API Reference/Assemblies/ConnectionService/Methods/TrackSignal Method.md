# TrackSignal Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~TrackSignal.html

---

Finds all connections on the same scheme as `oSourceConnection` that transmit the same signal.

Syntax

**C#**



public void TrackSignal( 

   Connection oSourceConnection,

   List<Connection> foundConnectionList

)

public:

void TrackSignal( 

   Connection^ oSourceConnection,

   List<Connection^>^ foundConnectionList

)


#### Parameters

*oSourceConnection*
:   Connection from which tracking signal is started.

*foundConnectionList*
:   List of connections that transmits the same signal as `oSourceConnection` and are on the same scheme.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if parameter `oSourceConnection` or `foundConnectionList` is `null` value. |
| [System.ArgumentException](#) | Throw if parameter `oSourceConnection` is invalid. |
