# EventHandlerNameFunction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerNameFunction.html

---

Functions of this type can be registered as event handlers in the class [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html).

Syntax

**C#**



public delegate void EventHandlerNameFunction( 

   IEventParameter pIEventParameter,

   string strNameOfEvent

)

public delegate void EventHandlerNameFunction( 

   IEventParameter^ pIEventParameter,

   String^ strNameOfEvent

)


#### Parameters

*pIEventParameter*


*strNameOfEvent*
:   The original name of the send event. Can be useful when I was registered for an wildcard event, p.e. "Test\*"
