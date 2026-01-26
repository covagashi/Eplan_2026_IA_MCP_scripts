# MDAnyPropertyId

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId.html

---

Utility class that represents id and index of P8 API properties.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDAnyPropertyId**

Syntax

**C#**



public sealed class MDAnyPropertyId

public ref class MDAnyPropertyId sealed


Remarks

The class contains also methods to convert between id number and corresponding [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.Properties.html). The only valid [Id](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~Id.html) value range comes from mentioned enum, that is why [Id](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~Id.html) property is read only.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDAnyPropertyId Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~_ctor().html) | Default constructor. Creates MDAnyPropertyId object. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AsMDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~AsMDPartsDatabaseItem.html) |  |
| Public Property | [AsMDSymbol](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~AsMDSymbol.html) |  |
| Public Property | [AsMDSymbolLibrary](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~AsMDSymbolLibrary.html) |  |
| Public Property | [AsMDSymbolVariant](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~AsMDSymbolVariant.html) |  |
| Public Property | [Definition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~Definition.html) | Definition of property. |
| Public Property | [Id](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~Id.html) | Integer id of this property. |
| Public Property | [Index](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~Index.html) | Index of the property. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~Dispose().html) | Destructor for deterministic finalization of MDAnyPropertyId object. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~op_Equality.html) | Equality operator |
| public Operator [Implicit Type Conversion](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAnyPropertyId~op_Implicit.html) | Overloaded. Converts the specified property number into MDAnyProjectId object. |


