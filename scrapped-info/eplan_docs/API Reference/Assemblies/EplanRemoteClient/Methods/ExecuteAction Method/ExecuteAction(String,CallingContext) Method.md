# ExecuteAction(String,CallingContext) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~ExecuteAction(String,CallingContext).html

---

Call an action.

Syntax

**C#**



public bool ExecuteAction( 

   string strAction,

   ref CallingContext context

)

public:

bool ExecuteAction( 

   String^ strAction,

   CallingContext^% context

)


#### Parameters

*strAction*
:   Action name or action name and all used parameters and values. Parameters and values could be set in calling Context.

*context*
:   Calling context.

#### Return Value

Returns true if Action is called successfully. Otherwise returns false.

Remarks

If the action did not succeed, an error message is reported in the calling context. In which mode this call is executed, synchronously or asynchronously, depends on the SynchronousMode property. Per default all calls are executed asynchronously (except Connect). You can change this behavior by setting the SynchronousMode property to true in order to make synchronous calls. If the call is asynchronous, EPLAN application sends a completed-execution acknowledgment response when the call is completely executed. The property AsyncCallCompleted in EplanResponse is set to true.
