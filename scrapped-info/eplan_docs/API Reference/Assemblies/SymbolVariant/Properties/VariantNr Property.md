# VariantNr Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant~VariantNr.html

---

Returns number that identifies variant of a Symbol.

Syntax

**C#**



public int VariantNr {get;}

public:

property int VariantNr {

   int get();

}


#### Property Value

variant of the symbol

Remarks

Numbers are from range 0-7 and correspond with letters A-H in GUI. Additional number 16 is for a contact image. To check which variants are valid, please open window "Symbol selection" and select required symbol.
