# GetNetDefinitionPoints Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetNetDefinitionPoints.html

---

This function takes objects of class [NetDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint.html) and filters them with the given filter.

Syntax

**C#**



public NetDefinitionPoint[] GetNetDefinitionPoints( 

   PlacementsFilter filter

)

public:

array<NetDefinitionPoint^>^ GetNetDefinitionPoints( 

   PlacementsFilter^ filter

)


#### Parameters

*filter*
:   a [PlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html), can be `null`

#### Return Value

\* [NetDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint.html)s matching given [PlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html). \* All [NetDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
