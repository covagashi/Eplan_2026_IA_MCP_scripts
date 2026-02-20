# GetInterruptionPointsWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetInterruptionPointsWithCF.html

---

Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given custom filter.

Syntax

**C#**



public InterruptionPoint[] GetInterruptionPointsWithCF( 

   ICustomFilter filter

)

public:

array<InterruptionPoint^>^ GetInterruptionPointsWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given custom filter. \* All [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
