# EventHandler

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html

---

Base class to handle events.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.EventHandler**

Syntax

**C#**



[ComSourceInterfaces(Eplan.EplApi.ApplicationFramework.IEplanEvents)]

public class EventHandler

[ComSourceInterfaces(Eplan.EplApi.ApplicationFramework.IEplanEvents)]

public ref class EventHandler


Remarks

If you want to respond to Eplan events from a remoting client, you should use a local event handler object of the [EventHandlerWrapper](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper.html) type.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EventHandler Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~_ctor.html) | Overloaded. |



Public Fields

|  | Name | Description |
| --- | --- | --- |
| Public Field | [EplanEvent](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~EplanEvent.html) | This event is raised whenever an event with the desired name occurs in Eplan. |
| Public Field | [EplanNameEvent](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~EplanNameEvent.html) | This event is raised whenever an event with the desired name occurs in Eplan. The original name of the event is also given. |
| Public Field | [EplanNameEventResult](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~EplanNameEventResult.html) | This event is raised whenever an event with the desired name occurs in Eplan. The original name of the event is also given. Additional a return value is supported. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~Dispose().html) | Event handler is released. |
| Public Method | [RaiseEvent](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~RaiseEvent.html) | For internal use only. |
| Public Method | [RaiseEventResult](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~RaiseEventResult.html) | For internal use only. |
| Public Method | [SetEvent](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~SetEvent.html) | Defines for which event the [IEplanEvents](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplanEvents.html) is raised. |



Public Events

|  | Name | Description |
| --- | --- | --- |
| Public Event | [NameEvent](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~NameEvent_EV.html) | This event is raised whenever an event with the desired name occurs in Eplan. |


