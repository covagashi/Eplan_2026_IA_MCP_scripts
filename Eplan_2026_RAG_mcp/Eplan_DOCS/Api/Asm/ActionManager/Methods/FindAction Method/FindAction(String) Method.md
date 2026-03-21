# FindAction(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager~FindAction(String).html

---

This function searches for an action registered in the system.

Syntax

**C#**



public Action FindAction( 

   string strNameOfAction

)

public:

Action^ FindAction( 

   String^ strNameOfAction

)


#### Parameters

*strNameOfAction*
:   Name of the action you search for.

#### Return Value

Returns a reference to a [Action](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html) or NULL in case no action with this name exists in the system.
