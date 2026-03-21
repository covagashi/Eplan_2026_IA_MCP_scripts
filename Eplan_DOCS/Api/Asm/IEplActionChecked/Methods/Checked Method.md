# Checked Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionChecked~Checked.html

---

One action can have the state on off or mixed. Return 0 for off, 1 for on, and 2 for mixed.

Syntax

**C#**



int Checked( 

   string strActionName,

   ActionCallingContext actionContext

)

int Checked( 

   String^ strActionName,

   ActionCallingContext^ actionContext

)


#### Parameters

*strActionName*
:   The name of this action

*actionContext*
:   The calling context.

#### Return Value

0: The return action has the state unchecked. 1: The return action has the state checked. 2: The return action has the state mixed.

Remarks

This function is called often and should work fast.
