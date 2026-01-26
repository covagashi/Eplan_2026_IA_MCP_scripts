# BoxedDevices Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~BoxedDevices.html

---

Returns all [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s placed on the page. If the filter was set up, returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching the filter.

Syntax

**C#**



public BoxedDevice[] BoxedDevices {get;}

public:

property array<BoxedDevice^>^ BoxedDevices {

   array<BoxedDevice^>^ get();

}


#### Property Value

[BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s on the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |
