# Connect(String,String,TimeSpan) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~Connect(String,String,TimeSpan).html

---

Connect to Eplan Server.

Syntax

**C#**



void Connect( 

   string strCompterName,

   string strPort,

   TimeSpan interval

)

void Connect( 

   String^ strCompterName,

   String^ strPort,

   TimeSpan interval

)


#### Parameters

*strCompterName*
:   Name or TCP-IP of the computer on which Eplan is running.

*strPort*
:   Port number used from Eplan Service.

*interval*
:   Waiting time of the connecting process. If the connecting time exceeds the value interval a CommunicationException will be thrown.
