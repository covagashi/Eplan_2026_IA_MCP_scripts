# GetBaseSymbolFromSpecifiedSymbolLibrary Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~GetBaseSymbolFromSpecifiedSymbolLibrary.html

---

Gets a base symbol for this function definition that may exist in the given symbol library. This method is useful if this function definition object is initialized without any reference to a project (i.e. initialized with a library from system master data)

Syntax

**C#**



public Symbol GetBaseSymbolFromSpecifiedSymbolLibrary( 

   SymbolLibrary symbolLibrary

)

public:

Symbol^ GetBaseSymbolFromSpecifiedSymbolLibrary( 

   SymbolLibrary^ symbolLibrary

)


#### Parameters

*symbolLibrary*
:   A symbol library to get a symbol from. This may be a library from system master data (i.e. without any reference to a project).

#### Return Value

[Eplan.EplApi.DataModel.MasterData.Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html) from the given symbol library.
