# InterconnectDevices(ArrayList,ArrayList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~InterconnectDevices(ArrayList,ArrayList).html

---

Interconnect devices like in dialog "Interconnect devices".

Syntax

**C#**



public Connection[] InterconnectDevices( 

   ArrayList arrPinsSource,

   ArrayList arrPinsTarget

)

public:

array<Connection^>^ InterconnectDevices( 

   ArrayList^ arrPinsSource,

   ArrayList^ arrPinsTarget

)


#### Parameters

*arrPinsSource*
:   List of pins. Sources of the new connections.

*arrPinsTarget*
:   List of pins. Targets of the new connections.

#### Return Value

Array of new created connections[Eplan.EplApi.DataModel.Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html).

Exceptions

| Exception | Description |
| --- | --- |
| **ApplicationException** | An internal interface necessary for the function could not be created. |

Remarks

Without parameter "cable", the new Connections are not of type "wire in cable"
