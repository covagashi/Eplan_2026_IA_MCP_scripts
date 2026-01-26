# BaseSymbol Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~BaseSymbol.html

---

Gets the best fitting SymbolVariant for this FunctionDefinition. This SymbolVariant can be used to insert SymbolReferences with not yet any SymbolVariant assigned onto pages. This is useful e.g. for InsertInteractions in GED

Syntax

**C#**



public SymbolVariant BaseSymbol {get;}

public:

property SymbolVariant^ BaseSymbol {

   SymbolVariant^ get();

}


#### Property Value

SymbolVariant fitting to the FunctionDefinition
