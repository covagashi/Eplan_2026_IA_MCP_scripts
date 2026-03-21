# GetPLCTerminalsWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPLCTerminalsWithFilterScheme.html

---

Returns [Eplan.EplApi.DataModel.EObjects.Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html) matching the given filter from PLC navigator.

Syntax

**C#**



public Terminal[] GetPLCTerminalsWithFilterScheme( 

   string strFilterScheme

)

public:

array<Terminal^>^ GetPLCTerminalsWithFilterScheme( 

   String^ strFilterScheme

)


#### Parameters

*strFilterScheme*
:   Name of a filter scheme in the PLC navigator.

    If an empty string is passed, a filter scheme currently set in GUI will be used. If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |
