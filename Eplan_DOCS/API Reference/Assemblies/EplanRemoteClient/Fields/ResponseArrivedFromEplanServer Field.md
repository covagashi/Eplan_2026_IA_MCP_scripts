# ResponseArrivedFromEplanServer Field

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~ResponseArrivedFromEplanServer.html

---

Handler to receive Eplan server notifications.

Syntax

**C#**



public OnResponseArrivedHandler ResponseArrivedFromEplanServer

public:

OnResponseArrivedHandler^ ResponseArrivedFromEplanServer


Example

myEplanClient.ResponseArrivedFromEplanServer += OnResponseArrivedHandler; static void OnResponseArrivedHandler(EplanResponse response) { //Handle Server response. }
