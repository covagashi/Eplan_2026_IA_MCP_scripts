# GetChecked Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~GetChecked.html

---

Returns 'checked' state of an action

Syntax

**C#**



public int GetChecked( 

   ActionCallingContext oCallingContext,

   string strActionWithParameters

)

public:

int GetChecked( 

   ActionCallingContext^ oCallingContext,

   String^ strActionWithParameters

)


#### Parameters

*oCallingContext*
:   Used to pass parameters to an action and to receive return values of the action

*strActionWithParameters*
:   Action name with parameters

Remarks

Can be used to simulate 'checkbox' or 'radio' style of a control bound to the action
