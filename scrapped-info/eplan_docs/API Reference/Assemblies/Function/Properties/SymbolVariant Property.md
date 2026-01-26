# SymbolVariant Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SymbolVariant.html

---

Specifies [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) assigned to this SymbolReference.

Syntax

**C#**



public override SymbolVariant SymbolVariant {get; set;}

public:

property SymbolVariant^ SymbolVariant {

   SymbolVariant^ get() override;

   void set (    SymbolVariant^ value) override;

}


#### Property Value

[Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) assigned to this SymbolReference

`null` when there is no [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) assigned to this Function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) cannot be read |
