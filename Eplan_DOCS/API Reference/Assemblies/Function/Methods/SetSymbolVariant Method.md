# SetSymbolVariant Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SetSymbolVariant.html

---

Sets symbol variant for Function.

Syntax

**C#**



public void SetSymbolVariant( 

   SymbolVariant pNewSymbolVariant,

   bool bUseLogicalDefinitionFromSymbol

)

public:

void SetSymbolVariant( 

   SymbolVariant^ pNewSymbolVariant,

   bool bUseLogicalDefinitionFromSymbol

)


#### Parameters

*pNewSymbolVariant*
:   Symbol variant to set

*bUseLogicalDefinitionFromSymbol*
:   Determines if logical definition from symbol should be used

Remarks

This method allows to set [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SymbolVariant.html) for function. Boolean parameter defines if logical definition should be taken from symbol. This logical definition have is responsible for, for example: [Pins](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Pins.html) data of Function.
