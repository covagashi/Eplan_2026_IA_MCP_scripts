# PlugStrips Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PlugStrips.html

---

Returns all [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s placed on the page. If the filter was set up, returns [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s matching the filter.

Syntax

**C#**



public PlugStrip[] PlugStrips {get;}

public:

property array<PlugStrip^>^ PlugStrips {

   array<PlugStrip^>^ get();

}


#### Property Value

[Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s placed on the page. If the filter was set up, returns [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s on the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |
