# PLCs Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PLCs.html

---

Returns all [Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)s placed on the page. If the filter was set up, returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching the filter.

Syntax

**C#**



public PLC[] PLCs {get;}

public:

property array<PLC^>^ PLCs {

   array<PLC^>^ get();

}


#### Property Value

[Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)s on the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |
