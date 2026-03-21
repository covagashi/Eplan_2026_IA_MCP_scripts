# IEplanRemoteClient

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient.html

---

Base interface for the communication with Eplan Server.

Syntax

**C#**



[Guid("155A4EA7-AB45-4c69-9B72-F6CB94BC6323")]

[ComVisible(true)]

public interface IEplanRemoteClient

[Guid("155A4EA7-AB45-4c69-9B72-F6CB94BC6323")]

[ComVisible(true)]

public interface class IEplanRemoteClient

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [License](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~License.html) | License file name (\*.lis). This Property should be set before calling any StartEplan method. |
| Property | [Password](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~Password.html) | Password. This Property should be set before calling any StartEplan method. |
| Property | [SynchronousMode](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~SynchronousMode.html) | Sets and gets the Synchronous mode. |
| Property | [User](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~User.html) | User name. This Property should be set before calling any StartEplan method. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Connect](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~Connect.html) | Overloaded. Connect to Eplan Server. |
| Method | [Disconnect](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~Disconnect.html) | Disconnect from Eplan Server. |
| Method | [ExecuteAction](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~ExecuteAction.html) | Overloaded. Execute an action. |
| Method | [GetActiveEplanServersOnLocalMachine](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~GetActiveEplanServersOnLocalMachine.html) | Get Eplan Servers that are currently active on local machine. |
| Method | [GetInstalledEplanVersionsOnLocalMachine](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~GetInstalledEplanVersionsOnLocalMachine.html) | Get Eplan versions that are currently installed on local machine. |
| Method | [LockAllEplanObjects](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~LockAllEplanObjects.html) | Lock all objects in given project. |
| Method | [Ping](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~Ping.html) | Ping the Eplan Server. |
| Method | [SelectEplanObjects](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~SelectEplanObjects.html) | Selects objects in GED |
| Method | [StartEplan](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~StartEplan.html) | Overloaded. Starts an Eplan instance. |
| Method | [StopEplan](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~StopEplan.html) | Stops the Eplan instance which is connected to the current client. |
| Method | [UnlockAllEplanObjects](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~UnlockAllEplanObjects.html) | Unlock all objects in given project. |


