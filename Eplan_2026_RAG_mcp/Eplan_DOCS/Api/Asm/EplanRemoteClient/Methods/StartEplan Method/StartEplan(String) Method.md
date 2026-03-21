# StartEplan(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~StartEplan(String).html

---

Starts an Eplan instance.

Syntax

**C#**



public EplanServerData StartEplan( 

   string strEplanFullPath

)

public:

EplanServerData^ StartEplan( 

   String^ strEplanFullPath

)


#### Parameters

*strEplanFullPath*
:   Full path of Eplan executable file.

#### Return Value

Information about the started Eplan remote server. If EPLAN application could not be started or if no communication could be established an exception Eplan.EplApi.RemoteClient.CommunicationException is thrown.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ObjectDisposedException](#) | The process object has already been disposed. |
| [System.IO.FileNotFoundException](#) | The PATH environment variable has a String containing quotes |
| [CommunicationException](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.CommunicationException.html) | EPLAN application could not be started or no communication is possible. |
