# Variant Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Variant.html

---

Index operator to get a variant by its name. Valid names are "A" or "a" through "H" or "h".

Syntax

**C#**



public MDSymbolVariant this[ 

   string variantName

]; {get;}

public:

property MDSymbolVariant^ default [String^] {

   MDSymbolVariant^ get(String^ variantName);

}


#### Parameters

*variantName*
:   The variant's name.
