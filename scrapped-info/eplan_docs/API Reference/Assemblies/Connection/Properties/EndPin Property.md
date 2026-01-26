# EndPin Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndPin.html

---

Returns the end [Pin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html) of this connection, if such exists (i.e. if the connection is connected on the target side). Otherwise, NULL is returned.

Syntax

**C#**



public virtual Pin EndPin {get;}

public:

virtual property Pin^ EndPin {

   Pin^ get();

}

