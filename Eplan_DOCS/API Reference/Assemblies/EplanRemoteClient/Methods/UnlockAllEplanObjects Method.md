# UnlockAllEplanObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~UnlockAllEplanObjects.html

---

Unlock all objects in given project.

Syntax

**C#**



public EplanResponse UnlockAllEplanObjects( 

   string strFullProjectName

)

public:

EplanResponse^ UnlockAllEplanObjects( 

   String^ strFullProjectName

)


#### Parameters

*strFullProjectName*
:   Full link file name of the project.

#### Return Value

Returns an EplanResponse object.

Remarks

In which mode this call is executed, synchronously or asynchronously, depends on the SynchronousMode property. Per default all calls are executed asynchronously (except Connect). You can change this behavior by setting the SynchronousMode property to true in order to make synchronous calls. If the call is asynchronous, EPLAN application sends a completed-execution acknowledgment response when the call is completely executed. The property AsyncCallCompleted in EplanResponse is set to true.
