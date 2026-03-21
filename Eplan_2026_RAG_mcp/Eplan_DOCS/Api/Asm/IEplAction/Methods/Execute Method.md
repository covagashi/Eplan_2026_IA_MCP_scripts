# Execute Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction~Execute.html

---

Called by the framework when the action is to be performed.

Syntax

**C#**



bool Execute( 

   ActionCallingContext oActionCallingContext

)

bool Execute( 

   ActionCallingContext^ oActionCallingContext

)


#### Parameters

*oActionCallingContext*
:   Parameter for this call, see [ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html).

#### Return Value

true, if the action was successfully performed; true, if the action was successfully registered in the system.
