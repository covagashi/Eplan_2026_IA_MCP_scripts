# GetCableUnitsWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetCableUnitsWithCF.html

---

Returns [Eplan.EplApi.DataModel.EObjects.CableUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit.html)es matching given filter.

Syntax

**C#**



public CableUnit[] GetCableUnitsWithCF( 

   ICustomFilter filter

)

public:

array<CableUnit^>^ GetCableUnitsWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [Eplan.EplApi.DataModel.EObjects.CableUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit.html)es matching given custom filter. \* All [Eplan.EplApi.DataModel.EObjects.CableUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit.html)es if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
