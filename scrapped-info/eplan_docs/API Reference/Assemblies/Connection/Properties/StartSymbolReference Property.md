# StartSymbolReference Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartSymbolReference.html

---

Returns the first of two [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this connection.

Syntax

**C#**



public SymbolReference StartSymbolReference {get;}

public:

property SymbolReference^ StartSymbolReference {

   SymbolReference^ get();

}


#### Property Value

- the first of two [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this connection,
- `null` when there is no SymbolReference on this end of the connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the SymbolReference from project. |
