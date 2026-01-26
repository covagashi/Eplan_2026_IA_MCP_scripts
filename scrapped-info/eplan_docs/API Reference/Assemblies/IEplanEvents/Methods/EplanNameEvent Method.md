# EplanNameEvent Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplanEvents~EplanNameEvent.html

---

this is the function prototype called when an Eplan event is raised.

Syntax

**C#**



void EplanNameEvent( 

   IEventParameter pIEventParameter,

   string strNameOfEvent

)

void EplanNameEvent( 

   IEventParameter^ pIEventParameter,

   String^ strNameOfEvent

)


#### Parameters

*pIEventParameter*
:   The eventparameter for this event

*strNameOfEvent*
:   The original name of the event. This is useful when registered for more events with wildcards.
