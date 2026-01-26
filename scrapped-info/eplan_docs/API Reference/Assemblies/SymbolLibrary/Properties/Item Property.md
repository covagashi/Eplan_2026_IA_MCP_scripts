# Item Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary~Item.html

---

Index operator to searching Symbol from given name.

Syntax

**C#**



public Symbol this[ 

   string symbolName

]; {get;}

public:

property Symbol^ default [String^] {

   Symbol^ get(String^ symbolName);

}


#### Parameters

*symbolName*
:   Name of symbol to search for.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.SymbolNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolNotFoundException.html) | Thrown when symbolName wasn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
