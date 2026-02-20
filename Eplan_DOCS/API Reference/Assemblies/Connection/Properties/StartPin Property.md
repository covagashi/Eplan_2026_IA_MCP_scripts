# StartPin Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartPin.html

---

Returns the start [Pin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html) of this connection, if such exists (i.e. if the connection is connected on the source side). Otherwise, NULL is returned.

Syntax

**C#**



public virtual Pin StartPin {get;}

public:

virtual property Pin^ StartPin {

   Pin^ get();

}

