# GetHarnessesWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetHarnessesWithFilterScheme.html

---

Returns [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)es matching given filter from wire harness navigator.

Syntax

**C#**



public Harness[] GetHarnessesWithFilterScheme( 

   string strFilterScheme

)

public:

array<Harness^>^ GetHarnessesWithFilterScheme( 

   String^ strFilterScheme

)


#### Parameters

*strFilterScheme*
:   Scheme-name of filter wire harness navigator

#### Return Value

\* If scheme-name is empty, the current filter scheme will be used. \* If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |
