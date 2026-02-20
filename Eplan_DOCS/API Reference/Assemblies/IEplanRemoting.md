# IEplanRemoting

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting.html

---

Eplan Communication interface

Syntax

**C#**



public interface IEplanRemoting

public interface class IEplanRemoting

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Connect](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~Connect.html) | Connect to service. |
| Method | [DisableSynchronizingCalls](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~DisableSynchronizingCalls.html) | Disable synchronizing calls. The execution of remote calls are synchronized in EPLAN. A remote call is executed only if the EPLAN Application is in an idle situation and there is no action running. Otherwise the call will wait until the EPLAN application is idle and no action is running. This property can be used to disable this mode. If calls synchronization is disabled, remote calls are executed in EPLAN although the EPLAN application is not in an idle situation. |
| Method | [Disconnect](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~Disconnect.html) | Disconnect from service. |
| Method | [ExecuteAction](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~ExecuteAction.html) | Execute an action synchronously. |
| Method | [ExecuteActionAsynch](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~ExecuteActionAsynch.html) | Execute an action asynchronously. |
| Method | [LockUnlockAllObjects](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~LockUnlockAllObjects.html) | Lock or unlock all Objects. |
| Method | [LockUnlockAllObjectsAsynch](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~LockUnlockAllObjectsAsynch.html) | Lock or unlock all Objects. |
| Method | [Ping](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~Ping.html) | Ping a service. |
| Method | [SelectObjects](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~SelectObjects.html) | Select Objects in Ged. |
| Method | [SelectObjectsAsynch](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~SelectObjectsAsynch.html) | Select Objects in Ged. |


