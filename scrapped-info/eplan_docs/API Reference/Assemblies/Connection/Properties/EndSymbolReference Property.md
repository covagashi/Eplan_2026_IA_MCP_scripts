# EndSymbolReference Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndSymbolReference.html

---

Returns the second of two [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this connection.

Syntax

**C#**



public SymbolReference EndSymbolReference {get;}

public:

property SymbolReference^ EndSymbolReference {

   SymbolReference^ get();

}


#### Property Value

- the second of two [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)s connected by this connection,
- `null` when there is no SymbolReference on this end of the connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the SymbolReference from project. |
