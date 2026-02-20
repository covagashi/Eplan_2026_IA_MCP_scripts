# IsFixedDevice Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~IsFixedDevice.html

---

Checks if device to which connection is assign is fixed or not.

Syntax

**C#**



public bool IsFixedDevice {get;}

public:

property bool IsFixedDevice {

   bool get();

}


Remarks

If device is fixed no [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) can be added/changed/removed from device of this connection. The same is with properties FUNC\_ARTICLE\_PARTNR and FUNC\_ARTICLE\_COUNT.
