# GetFunctions(FunctionsFilter,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctions(FunctionsFilter,Boolean).html

---

Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given filter. If "bWithConnectionDefinitionPoints" is true, returns [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)s matching given filter, too.

Syntax

**C#**



public Function[] GetFunctions( 

   FunctionsFilter filter,

   bool bWithConnectionDefinitionPoints

)

public:

array<Function^>^ GetFunctions( 

   FunctionsFilter^ filter,

   bool bWithConnectionDefinitionPoints

)


#### Parameters

*filter*
:   a [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html), can be `null`

*bWithConnectionDefinitionPoints*
:   defines, if text="Eplan.EplApi.DataModel.ConnectionDefinitionPoint"/>s should be found, too

#### Return Value

\* [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s and (if "bWithConnectionDefinitionPoints" is true) [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)s matching given [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html). \* All [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s and (if "bWithConnectionDefinitionPoints" is true) [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
