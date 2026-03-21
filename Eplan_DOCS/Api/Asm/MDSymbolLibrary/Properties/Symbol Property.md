# Symbol Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Symbol.html

---

Index operator to get a symbol by its name.

Syntax

**C#**



public MDSymbol this[ 

   string symbolName

]; {get;}

public:

property MDSymbol^ default [String^] {

   MDSymbol^ get(String^ symbolName);

}


#### Parameters

*symbolName*
:   Name of the symbol to get.
