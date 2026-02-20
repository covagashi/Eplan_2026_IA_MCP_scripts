# DisableSynchronizingCalls Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~DisableSynchronizingCalls.html

---

Disable synchronizing calls. The execution of remote calls are synchronized in EPLAN. A remote call is executed only if the EPLAN Application is in an idle situation and there is no action running. Otherwise the call will wait until the EPLAN application is idle and no action is running. This property can be used to disable this mode. If calls synchronization is disabled, remote calls are executed in EPLAN although the EPLAN application is not in an idle situation.

Syntax

**C#**



void DisableSynchronizingCalls( 

   bool bDisable

)

void DisableSynchronizingCalls( 

   bool bDisable

)


#### Parameters

*bDisable*
