# GetBoxedDevices Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetBoxedDevices.html

---

Returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching given filter.

Syntax

**C#**



public BoxedDevice[] GetBoxedDevices( 

   FunctionsFilter filter

)

public:

array<BoxedDevice^>^ GetBoxedDevices( 

   FunctionsFilter^ filter

)


#### Parameters

*filter*
:   a [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html), can be `null`

#### Return Value

\* [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching given [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html). \* All [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
