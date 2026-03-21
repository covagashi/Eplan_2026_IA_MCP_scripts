# StartEplan(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~StartEplan(String,String).html

---

Starts an Eplan instance with arguments.

Syntax

**C#**



EplanServerData StartEplan( 

   string strEplanFullPath,

   string arguments

)

EplanServerData^ StartEplan( 

   String^ strEplanFullPath,

   String^ arguments

)


#### Parameters

*strEplanFullPath*
:   Full path of Eplan executable file.

*arguments*
:   Command-line arguments to pass when starting the process.

#### Return Value

Information about the started Eplan remote server. If EPLAN application could not be started or if no communication could be established an exception Eplan.EplApi.RemoteClient.CommunicationException is thrown.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | \Parameters are invalid. |
| [System.ObjectDisposedException](#) | The process object has already been disposed. |
| [System.IO.FileNotFoundException](#) | The PATH environment variable has a String containing quotes |
| [CommunicationException](Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.CommunicationException.html) | EPLAN application could not be started or no communication is possible. |
