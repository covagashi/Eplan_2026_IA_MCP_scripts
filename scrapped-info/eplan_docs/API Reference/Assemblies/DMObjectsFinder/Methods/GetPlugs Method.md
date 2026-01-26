# GetPlugs Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugs.html

---

Returns [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s matching given filter.

Syntax

**C#**



public Plug[] GetPlugs( 

   FunctionsFilter filter

)

public:

array<Plug^>^ GetPlugs( 

   FunctionsFilter^ filter

)


#### Parameters

*filter*
:   a [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html), can be `null`

#### Return Value

\* [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s matching given [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html). \* All [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
