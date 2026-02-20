# SetEvent Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler~SetEvent.html

---

Defines for which event the [IEplanEvents](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplanEvents.html) is raised.

Syntax

**C#**



public void SetEvent( 

   string strEventName

)

public:

void SetEvent( 

   String^ strEventName

)


#### Parameters

*strEventName*
:   Events with this name are edited through this event handler object.

Example

Define the event to respond to

**C#**

```
// Generate an event handler object

Eplan.EplApi.ApplicationFramework.EventHandler myHandler= new Eplan.EplApi.ApplicationFramework.EventHandler();

// The program should respond to this event

myHandler.SetEvent("onActionStart.String.*");
```
