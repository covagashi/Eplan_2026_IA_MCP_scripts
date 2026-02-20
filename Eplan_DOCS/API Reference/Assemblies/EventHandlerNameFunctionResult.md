# EventHandlerNameFunctionResult

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerNameFunctionResult.html

---

Functions of this type can be registered as event handlers in the class [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html).

Syntax

**C#**



public delegate long EventHandlerNameFunctionResult( 

   IEventParameter pIEventParameter,

   string strNameOfEvent

)

public delegate int64 EventHandlerNameFunctionResult( 

   IEventParameter^ pIEventParameter,

   String^ strNameOfEvent

)


#### Parameters

*pIEventParameter*


*strNameOfEvent*
:   The original name of the send event. Can be useful when I was registered for an wildcard event, p.e. "Test\*"

#### Return Value

the return value of your event. When there are more handlers the result value is the bitwise or of all results.
