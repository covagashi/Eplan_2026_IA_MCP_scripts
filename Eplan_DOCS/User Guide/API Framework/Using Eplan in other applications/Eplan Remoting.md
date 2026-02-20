# Eplan Remoting

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/EPLANRemoting.html

---

## Introduction to Remoting

Eplan remoting is a part of the API that enables users to connect to an Eplan platform variant and control it in remote way. It allows you to execute actions and some P8 operations in the remotely. Internally it uses gRPC and protocol buffers (protobuf) technology.

## Libraries

Eplan remoting consists of the following libraries:

**Internal** libraries:

- Eplan.EplApi.RemoteClientu.dll  (namespace [Eplan.EplApi.RemoteClient](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient_namespace.html))
- Eplan.EplApi.Remotingu.dll  (namespace [Eplan.EplApi.Remoting](Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting_namespace.html))

**External** libraries:

- Google.Protobuf.dll
- Grpc.Core.Api.dll
- Grpc.Core.dll
- Grpc\_csharp\_ext.x64.dll

**.NET System** libraries:

- System.Runtime.CompilerServices.Unsafe
- System.Runtime.Remoting

Warning!  
It is possible to compile a program without the  System.Runtime.CompilerServices.Unsafe  library, but it will not work at all.

The  Grpc\_csharp\_ext.x64.dll  is a runtime DLL that is used by the  Grpc.Core  and it is necessary to integrate it to the project. There are two ways to integrate it correctly:  
Either you copy it into the build folder or add it to the project as an existing item (in Visual Studio Add > Exiting Item... or standard shortcut Shift + Alt + A).

Notice:  
The name of the DLL must be entered explicitly in the search field.

When added, please set the property Copy to Output Directory to "Copy always":

All the DLLs are stored in the Eplan platform  BIN  folder. Below are examples how to use it.

## Eplan Remoting Overview

To use remoting, please proceed as follows:

### Precondition of use

As a prerequisite, the Eplan variant must be started as a remoting server (without the  /NoRemoting  parameter).

The default port for an Eplan instance is 49152. It is possible to start a gRPC server on a different port by using the   /EplanServerPort  parameter when starting P8 application via the command line. The port should be in the range from 49152 to 65535.

**Troubleshooting port problems**:

If you are having problems conneting to a supposedly free port in the specified range, you might find the reason for this in the Windows exluded port ranges. To query the range of ports that is currently excluded, run the following Netshell command:

netsh int <ipv4|ipv6> show excludedportrange [protocol=]tcp|udp [[store=]active|persistent]

If your designated port is in this list, you might be able to free it using this command (run as administrator):

net stop winnat && net start winnat

### Connection

First, a connection must be established form the client application (a .NET program written by the API user) to an existing Eplan instance that is available in the network. To open a new session, you have to connect your client to one of the existing P8 instances (to be precise to the gRPC server that is embedded inside it). The server can run locally or remotely.

### Opertations

After connecting, you can execute P8 actions (synchronously or asynchronously) and some P8 operations remotely. You can also pass or get parameters using an action calling context.

### Disconnection

Finally, to close your remote session, you have to disconnect. It is important to close the connection when all operations are finished.

# Remoting Code Examples

The following examples show how to use Eplan remoting.

### Establishing a connection with the localhost

```csharp
EplanRemoteClient oClient = new EplanRemoteClient();
 bool bConnected = oClient.Connect("localhost", "49152");  // Default port for Eplan instance is 49152
```

### Establishing a connection with a remote server

```csharp
EplanRemoteClient oClient = new EplanRemoteClient();
 bool bConnected = oClient.Connect("remote_server", "49152", new TimeSpan(0, 0, 0, 5));  // Wait 5 seconds
```

### Getting installed local servers

```csharp
List<EplanServerData> oInstalledEplanVersions = new List<EplanServerData>();
 oClient.GetInstalledEplanVersionsOnLocalMachine(out oInstalledEplanVersions);
 foreach (EplanServerData oVersion in oInstalledEplanVersions)
    Console.WriteLine(oVersion.EplanVariant + "," + oVersion.EplanVersion + "," + (oVersion.Is64Bit ? "64" : "32");
```

### Listing servers on a local machine

```csharp
List<EplanServerData> oActiveEplanVersions = new List<EplanServerData>();
 oClient.GetActiveEplanServersOnLocalMachine(out oActiveEplanVersions);
 foreach (EplanServerData oVersion in oActiveEplanVersions)
    Console.WriteLine(oVersion.EplanVariant + "," + oVersion.EplanVersion + "," + oVersion.ServerPort);
```

### Start an Eplan instance locally from a client

```csharp
List<EplanServerData> oInstalledEplanVersions = new List<EplanServerData>();
 oClient.GetInstalledEplanVersionsOnLocalMachine(out oInstalledEplanVersions);
 EplanServerData oConnected = oClient.StartEplan(oInstalledEplanVersions[0].EplanPath);
```

To make sure that the Eplan server was started, please check the registry key  HKEY\_CURRENT\_USER\Software\EPLAN\RemoteServer\<port\_number>.

### Calling an action

```csharp
bool oResp = oClient.ExecuteAction("XPartsManagementStart");
```

### Calling an action in an asynchronous mode

```csharp
oClient.SynchronousMode = false;
 oClient.ResponseArrivedFromEplanServer += onCallbackArrivedFromEplan;
 oClient.ExecuteAction("XPartsManagementStart");
```

In this case, the program starts an action and continues running. onCallbackArrivedFromEplan method is called after action finished.

### Calling an action in synchronous mode

This example shows how to get input from a user using context:

```csharp
oClient.SynchronousMode = true;
 CallingContext oCallingContext = new CallingContext();
 oClient.ExecuteAction("XPamSelectPart", ref oCallingContext);
```

In this case, the program waits until the action execution is finished.

### Making a selection

```csharp
StringCollection oObjects = new StringCollection();
 oObjects.Add(@"17/688");
 EplanResponse oResponse = oClient.SelectEplanObjects(@"$(MD_PROJECTS)\EPLAN_Sample_Project.elk", oObjects, true);
```

### Disconnection

```csharp
oClient.Disconnect();
```

Don't forget to close the connection when all operations are finished.
