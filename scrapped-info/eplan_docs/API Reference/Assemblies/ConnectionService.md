# ConnectionService

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService.html

---

Class providing connection functionality: Placing , designating, re-aligning, re-formatting, and deleting connection definition points.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.ConnectionService**

Syntax

**C#**



public class ConnectionService

public ref class ConnectionService

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ConnectionService Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AlignAndFormatConnectionDefinitionPoints](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~AlignAndFormatConnectionDefinitionPoints.html) | Overloaded. function to re-align and re-format connection definition points. |
| Public Method | [DeleteConnectionDefinitionPoints](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~DeleteConnectionDefinitionPoints.html) | Overloaded. Delete wire designations and connection definition points. |
| Public Method | [DesignateConnections](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~DesignateConnections.html) | Overloaded. Designate connections (wires) with connection definition point. |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~Dispose().html) | Destructor |
| Public Method | [ExportProductionWiring](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~ExportProductionWiring.html) | Overloaded. Exports manufacturing data for wire fabrication machines. |
| Public Method | [GenerateListOfUnusedConnections](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~GenerateListOfUnusedConnections.html) | Generates list of unused or deleted connection from project. |
| Public Method | [InterconnectDevices](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~InterconnectDevices.html) | Overloaded. Interconnect devices like in dialog "Interconnect devices". |
| Public Method | [PlaceConnectionDefinitionPoints](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~PlaceConnectionDefinitionPoints.html) | Overloaded. Function for placing connection definition points (CDPs). |
| Public Method | [SwapSourceAndTarget](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~SwapSourceAndTarget.html) | Exchanges the source and target properties of given connection. |
| Public Method | [TrackNet](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~TrackNet.html) | Finds all connections in the same net as `oSourceConnection`. |
| Public Method | [TrackPotential](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~TrackPotential.html) | Finds all connections which are in the same circuit as `oSourceConnection` and have the same potential. |
| Public Method | [TrackSignal](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~TrackSignal.html) | Finds all connections on the same scheme as `oSourceConnection` that transmit the same signal. |


