# Enabled Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionEnable~Enabled.html

---

One action can be enabled or disabled. Return true when it is enabled.

Syntax

**C#**



bool Enabled( 

   string strActionName,

   ActionCallingContext actionContext

)

bool Enabled( 

   String^ strActionName,

   ActionCallingContext^ actionContext

)


#### Parameters

*strActionName*
:   The name of this action

*actionContext*
:   The calling context

#### Return Value

true: The return action is enabled.

Remarks

This function is called often and should work efficiently .
