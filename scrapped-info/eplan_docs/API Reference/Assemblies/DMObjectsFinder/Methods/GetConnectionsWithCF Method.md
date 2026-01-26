# GetConnectionsWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetConnectionsWithCF.html

---

Returns [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching given filter.

Syntax

**C#**



public Connection[] GetConnectionsWithCF( 

   ICustomFilter filter

)

public:

array<Connection^>^ GetConnectionsWithCF( 

   ICustomFilter^ filter

)


#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching given custom filter. \* All [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
