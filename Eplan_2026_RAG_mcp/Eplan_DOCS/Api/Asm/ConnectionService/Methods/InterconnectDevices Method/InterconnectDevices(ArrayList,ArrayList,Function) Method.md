# InterconnectDevices(ArrayList,ArrayList,Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~InterconnectDevices(ArrayList,ArrayList,Function).html

---

Interconnect devices like in dialog "Interconnect devices".

Syntax

**C#**



public Connection[] InterconnectDevices( 

   ArrayList arrPinsSource,

   ArrayList arrPinsTarget,

   Function cable

)

public:

array<Connection^>^ InterconnectDevices( 

   ArrayList^ arrPinsSource,

   ArrayList^ arrPinsTarget,

   Function^ cable

)


#### Parameters

*arrPinsSource*
:   List of pins. Sources of the new connections.

*arrPinsTarget*
:   List of pins. Targets of the new connections.

*cable*
:   Cable whose free wires are taken to connect the pins.

#### Return Value

Array of new created connections[Eplan.EplApi.DataModel.Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html).

Exceptions

| Exception | Description |
| --- | --- |
| **ApplicationException** | An internal interface necessary for the function could not be created. |
