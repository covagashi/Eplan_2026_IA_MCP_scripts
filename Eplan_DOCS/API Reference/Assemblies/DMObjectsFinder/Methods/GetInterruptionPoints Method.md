# GetInterruptionPoints Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetInterruptionPoints.html

---

Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given filter.

Syntax

**C#**



public InterruptionPoint[] GetInterruptionPoints( 

   InterruptionPointsFilter filter

)

public:

array<InterruptionPoint^>^ GetInterruptionPoints( 

   InterruptionPointsFilter^ filter

)


#### Parameters

*filter*
:   a [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html), can be `null`

#### Return Value

\* [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html). \* All [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
