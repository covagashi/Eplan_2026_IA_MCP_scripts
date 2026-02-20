# GetHarnesses Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetHarnesses.html

---

Returns [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)es matching given filter.

Syntax

**C#**



public Harness[] GetHarnesses( 

   FunctionsFilter filter

)

public:

array<Harness^>^ GetHarnesses( 

   FunctionsFilter^ filter

)


#### Parameters

*filter*
:   a [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html), can be `null`

#### Return Value

\* [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)es matching given [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html). \* All [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)es if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
