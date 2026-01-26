# GetFunctions(FunctionsFilter,Functions3DFilter) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctions(FunctionsFilter,Functions3DFilter).html

---

Returns array of 2D and 3D [IFunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IFunctionBase.html) matching given filter.

Syntax

**C#**



public IFunctionBase[] GetFunctions( 

   FunctionsFilter functionsFilter,

   Functions3DFilter function3DFilter

)

public:

array<IFunctionBase^>^ GetFunctions( 

   FunctionsFilter^ functionsFilter,

   Functions3DFilter^ function3DFilter

)


#### Parameters

*functionsFilter*
:   a [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html), can be `null`

*function3DFilter*
:   a [Functions3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Functions3DFilter.html), can be `null`

#### Return Value

\* Array of [IFunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IFunctionBase.html) matching given [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html) or [Functions3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Functions3DFilter.html). \* All [IFunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IFunctionBase.html) if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |

Remarks

The result does not contain [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) and [Eplan.EplApi.DataModel.E3D.InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html).
