# EventHandlerWrapper

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper.html

---

Event handler to process Eplan events in a remoting client. It is not possible to directly use the [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html) in a remoting client!

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.EventHandlerWrapper**

Syntax

**C#**



public class EventHandlerWrapper

public ref class EventHandlerWrapper


Example

Response to Eplan events in a remoting client

**C#**

```
Eplan.EplApi.ApplicationFramework.EventHandler oEventHandler = new Eplan.EplApi.ApplicationFramework.EventHandler();

oEventHandler.SetEvent("onActionStart.String.*");

Eplan.EplApi.ApplicationFramework.EventHandlerWrapper oWrapper= new Eplan.EplApi.ApplicationFramework.EventHandlerWrapper();

oWrapper.EplanEventLocally += new Eplan.EplApi.ApplicationFramework.EventHandlerFunction(oWrapper_EventHandlerFunctionLocally);

oEventHandler.EplanEvent += new Eplan.EplApi.ApplicationFramework.EventHandlerFunction(oWrapper.LocallyEventHandlerFunction);
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EventHandlerWrapper Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~_ctor.html) |  |



Public Fields

|  | Name | Description |
| --- | --- | --- |
| Public Field | [EplanEventLocally](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~EplanEventLocally.html) | Local event handler |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [InitializeLifetimeService](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~InitializeLifetimeService.html) | This object should live "forever." |
| Public Method | [LocallyEventHandlerFunction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~LocallyEventHandlerFunction.html) | This function of the local event handler is registered as a handler function of the remote event handler [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html). |


