# GetFunctionsWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctionsWithFilterScheme.html

---

Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) matching given filter from devices-navigator.

Syntax

**C#**



public Function[] GetFunctionsWithFilterScheme( 

   string strFilterScheme

)

public:

array<Function^>^ GetFunctionsWithFilterScheme( 

   String^ strFilterScheme

)


#### Parameters

*strFilterScheme*
:   Scheme-name of filter devices-navigator

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |

Remarks

\* If scheme-name is empty, the current filter scheme will be used. \* If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator. \* Function templates are not returned by this method.
