# Execute Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Execute.html

---

Performs the actual action.

Syntax

**C#**



public bool Execute( 

   ActionCallingContext oCallingContext

)

public:

bool Execute( 

   ActionCallingContext^ oCallingContext

)


#### Parameters

*oCallingContext*
:   Using this parameter generic parameters of variable number and different types can be passed to the action.

#### Return Value

'¢ TRUE: This function was completed successfully.  
'¢ FALSE: An error occurred while performing the action.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exceptions may occur while performing the action. All these exceptions are returned as BaseException. |

Remarks

Exceptions, which occur during the execution of an action can be retrieved from the ActionCallingContext by the GetException() method.
