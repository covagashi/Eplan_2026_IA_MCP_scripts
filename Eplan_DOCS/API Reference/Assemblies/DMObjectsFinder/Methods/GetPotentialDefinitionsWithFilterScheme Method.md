# GetPotentialDefinitionsWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPotentialDefinitionsWithFilterScheme.html

---

Returns [PotentialDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinition.html)s matching given filter from potentials-navigator.

Syntax

**C#**



public PotentialDefinition[] GetPotentialDefinitionsWithFilterScheme( 

   string strFilterScheme

)

public:

array<PotentialDefinition^>^ GetPotentialDefinitionsWithFilterScheme( 

   String^ strFilterScheme

)


#### Parameters

*strFilterScheme*
:   Scheme-name of filter potentials-navigator

#### Return Value

\* If scheme-name is empty, the current filter scheme will be used. \* If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |
