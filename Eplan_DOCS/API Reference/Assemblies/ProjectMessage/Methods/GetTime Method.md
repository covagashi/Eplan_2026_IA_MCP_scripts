# GetTime Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetTime.html

---

Returns the creation time of the message

Syntax

**C#**



public DateTime GetTime()

public:

DateTime GetTime();


Remarks

Some messages do not have this property set. In this case DateTime.MinValue object is returned. Please set USER.EsDMServices.EsMsgMgmtService.WriteUserAndTimeToAllMessages in order to write User and Time data to every message when it is created. This settings can be initialized only before first check run. Please restart EPLAN in order to initialize settings again.
