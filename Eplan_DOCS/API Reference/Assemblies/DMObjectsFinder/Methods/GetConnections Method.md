# GetConnections Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetConnections.html

---

Returns [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching given filter. If null parameter is passed, all the project's connection objects are returned. Note: In case no filter used, number of objects returned may be bigger than the number of connections visible in the GUI's connection navigator. The GUI's connection navigator by default shows connections of the following placement types only: - Circuit - CircuitSingleLine - Overview - PairCrossReference - ProcessAndInstrumentationDiagram - PanelLayout

Syntax

**C#**



public Connection[] GetConnections( 

   ConnectionsFilter filter

)

public:

array<Connection^>^ GetConnections( 

   ConnectionsFilter^ filter

)


#### Parameters

*filter*
:   a [ConnectionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter.html), can be `null`

#### Return Value

\* [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching given [ConnectionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter.html). \* All [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
