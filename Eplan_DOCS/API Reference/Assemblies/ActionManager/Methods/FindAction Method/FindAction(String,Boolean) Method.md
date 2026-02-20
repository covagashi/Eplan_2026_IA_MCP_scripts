# FindAction(String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager~FindAction(String,Boolean).html

---

This function searches for an action registered in the system.

Syntax

**C#**



public Action FindAction( 

   string strNameOfAction,

   bool bSilent

)

public:

Action^ FindAction( 

   String^ strNameOfAction,

   bool bSilent

)


#### Parameters

*strNameOfAction*
:   Name of the action you search for.

*bSilent*
:   true: no error is reported in the system errors when the action is not found.

#### Return Value

Returns a reference to a [Action](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html) or NULL in case no action with this name exists in the system.
