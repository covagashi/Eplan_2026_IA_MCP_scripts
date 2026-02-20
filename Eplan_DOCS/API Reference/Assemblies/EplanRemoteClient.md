# EplanRemoteClient

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient.html

---

Eplan Remoting Client used to communicate with an Eplan instance. Note that the binding name should be exactly "EplanRemotingClientBindingConfig" otherwise it will be ignored.

Inheritance Hierarchy

[System.Object](#)  
   Grpc.Core.ClientBase  
      Grpc.Core.ClientBase<T>  
            **Eplan.EplApi.RemoteClient.EplanRemoteClient**

Syntax

**C#**



[Guid("25B37226-6821-4493-B585-F805EFBC3146")]

[ComVisible(true)]

public class EplanRemoteClient : Eplan.EplApi.GrpcServer.EplanRemoting.EplanRemotingClient, IEplanRemoteClient

[Guid("25B37226-6821-4493-B585-F805EFBC3146")]

[ComVisible(true)]

public ref class EplanRemoteClient : public Eplan.EplApi.GrpcServer.EplanRemoting::EplanRemotingClient, IEplanRemoteClient

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EplanRemoteClient Constructor](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~_ctor.html) | Constructor. |



Public Fields

|  | Name | Description |
| --- | --- | --- |
| Public Field | [ResponseArrivedFromEplanServer](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~ResponseArrivedFromEplanServer.html) | Handler to receive Eplan server notifications. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Connected](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~Connected.html) |  |
| Public Property | [License](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~License.html) | License file name (\*.lis). |
| Public Property | [Password](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~Password.html) | Eplan log-in password used for Rights Management. |
| Public Property | [SynchronousMode](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~SynchronousMode.html) | Sets and gets the Synchronous mode. |
| Public Property | [User](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~User.html) | Eplan log-in user used for Rights Management. User settings will be used from this user. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Connect](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~Connect.html) | Overloaded. Connect to Eplan Server. |
| Public Method | [DisableSynchronizingCalls](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~DisableSynchronizingCalls.html) | Overloaded. Disable synchronizing calls. The execution of remote calls are synchronized in EPLAN. A remote call is executed only if the EPLAN Application is in an idle situation and there is no action running. Otherwise the call will wait until the EPLAN application is idle and no action is running. This property can be used to disable this mode. If calls synchronization is disabled, remote calls are executed in EPLAN although the EPLAN application is not in an idle situation. |
| Public Method | [Disconnect](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~Disconnect.html) | Overloaded. Disconnect from Eplan Server. |
| Public Method | [DisconnectInternal](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~DisconnectInternal.html) | Disconnect from Eplan Server. |
| Public Method | [Dispose](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~Dispose().html) | Dispose. |
| Public Method | [ExecuteAction](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~ExecuteAction.html) | Overloaded. Execute an action. |
| Public Method | [GetActiveEplanServersOnLocalMachine](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~GetActiveEplanServersOnLocalMachine.html) | Get Eplan Servers which are currently active on local machine. |
| Public Methodstatic (Shared in Visual Basic) | [GetFreePort](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~GetFreePort.html) | Returns first free port which can act as a tunnel for remote server. |
| Public Method | [GetInstalledEplanVersionsOnLocalMachine](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~GetInstalledEplanVersionsOnLocalMachine.html) | Get Eplan versions which are currently installed on local machine. |
| Public Methodstatic (Shared in Visual Basic) | [IsPortFree](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~IsPortFree.html) | Checks if the port is free. |
| Public Method | [LockAllEplanObjects](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~LockAllEplanObjects.html) | Lock all objects in given project. |
| Public Method | [Ping](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~Ping.html) | Overloaded. Ping the Eplan Server. |
| Public Method | [SelectEplanObjects](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~SelectEplanObjects.html) | Selects objects in GED |
| Public Method | [StartEplan](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~StartEplan.html) | Overloaded. Starts an Eplan instance. |
| Public Method | [StopEplan](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~StopEplan.html) | Stops the Eplan instance which is connected to the current client. |
| Public Method | [UnlockAllEplanObjects](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~UnlockAllEplanObjects.html) | Unlock all objects in given project. |
| Public Method | [WithHost](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~WithHost.html) | (Inherited from Grpc.Core.ClientBase<EplanRemoting.EplanRemotingClient>) |


