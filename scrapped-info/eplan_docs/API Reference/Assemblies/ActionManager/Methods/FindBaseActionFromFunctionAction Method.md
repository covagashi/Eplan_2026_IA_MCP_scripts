# FindBaseActionFromFunctionAction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager~FindBaseActionFromFunctionAction.html

---

This function searches the base action for an existing action in scripting. the base action has the same name, but a lower ordinal.

Syntax

**C#**



public Action FindBaseActionFromFunctionAction( 

   bool bSilent

)

public:

Action^ FindBaseActionFromFunctionAction( 

   bool bSilent

)


#### Parameters

*bSilent*
:   true: no error is reported in the system errors when the action is not found.

#### Return Value

Returns a reference to a [Action](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html) or NULL in case no action with this name exists in the system.
