# MDSymbol

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol.html

---

MDSymbol is a master data symbol stored in a symbol library. A Symbol is identified by an Id and a Name. A MDSymbol contains up to 8 MDSymbolVariant.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      **Eplan.EplApi.MasterData.MDSymbol**

Syntax

**C#**



[DefaultMember("Variant")]

public class MDSymbol : PropertiesAndHandleObject

[DefaultMember("Variant")]

public ref class MDSymbol : public PropertiesAndHandleObject


Example

It is possible to get MDSymbolVariant object from MDSymbol, by indexer :

**C#**

```
MDSymbol smbl = ...

MDSymbolVariant v = smbl["A"];
```

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [FunctionDefinitionCategory](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~FunctionDefinitionCategory.html) | Category of FunctionDefinition as enum value. |
| Public Property | [FunctionDefinitionGroup](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~FunctionDefinitionGroup.html) | Group of FunctionDefinition. |
| Public Property | [FunctionDefinitionId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~FunctionDefinitionId.html) | FunctionDefinition's ID. |
| Public Property | [Id](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Id.html) | Returns the Id of the Symbol. |
| Public Property | [Name](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Name.html) | Returns the Name of the Symbol. |
| Public Property | [PlacementType](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~PlacementType.html) | Returns the placement type of the Symbol. |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Properties.html) | .NET Property enabling access to P8 properties of the MDSymbol object. |
| Public Property | [PropertyPlacementsSchemas](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~PropertyPlacementsSchemas.html) |  |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Type.html) | Returns the Type of the Symbol. |
| Public Property | [Variant](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Variant.html) | Index operator to get a variant by its name. Valid names are "A" or "a" through "H" or "h". |
| Public Property | [Variants](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Variants.html) | a read only list of all MDSymbolVariants in the symbol |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddSymbolVariant](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~AddSymbolVariant.html) |  |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDSymbol object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [GetConnectionPoints](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~GetConnectionPoints.html) | Overloaded. Returns an array of connection points defined in the symbol's function definition. |
| Public Method | [Remove](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~Remove.html) | Removes the symbol out of the symbol library. |


