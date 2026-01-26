# ExecuteAction(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~ExecuteAction(String).html

---

Execute an action.

Syntax

**C#**



bool ExecuteAction( 

   string strFullAction

)

bool ExecuteAction( 

   String^ strFullAction

)


#### Parameters

*strFullAction*
:   Action name or action name and all used parameters and values.

#### Return Value

Returns true if Action is called successfully. Otherwise returns false.

Remarks

In which mode this call is executed, synchronously or asynchronously, depends on the SynchronousMode property. Per default all calls are executed asynchronously (except Connect). You can change this behavior by setting the SynchronousMode property to true in order to make synchronous calls. If the call is asynchronous, EPLAN application sends a completed-execution acknowledgment response when the call is completely executed. The property AsyncCallCompleted in EplanResponse is set to true.
