# Item Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol~Item.html

---

Index operator to looking for SymbolVariant from given index.

Syntax

**C#**



public SymbolVariant this[ 

   int variantIdx

]; {get;}

public:

property SymbolVariant^ default [int] {

   SymbolVariant^ get(int variantIdx);

}


#### Parameters

*variantIdx*

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.SymbolVariantNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolVariantNotFoundException.html) | Thrown when specified variant wasn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
