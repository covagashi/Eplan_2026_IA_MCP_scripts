# GetBoxedDevicesWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetBoxedDevicesWithCF.html

---

Returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching given filter.

Syntax

**C#**



public BoxedDevice[] GetBoxedDevicesWithCF( 

   ICustomFilter filter

)

public:

array<BoxedDevice^>^ GetBoxedDevicesWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching given custom filter. \* All [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
