# GetPlugsWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugsWithCF.html

---

Returns [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s matching given filter.

Syntax

**C#**



public Plug[] GetPlugsWithCF( 

   ICustomFilter filter

)

public:

array<Plug^>^ GetPlugsWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s matching given custom filter. \* All [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
