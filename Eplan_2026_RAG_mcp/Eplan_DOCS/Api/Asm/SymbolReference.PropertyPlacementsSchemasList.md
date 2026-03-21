# SymbolReference.PropertyPlacementsSchemasList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList.html

---

A structure representing a property placements schemes.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.SymbolReference.PropertyPlacementsSchemasList**

Syntax

**C#**



public class SymbolReference.PropertyPlacementsSchemasList

public ref class SymbolReference.PropertyPlacementsSchemasList

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [All](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~All.html) | Returns an array of SymbolReference::PropertyPlacementsSchema elements representing predefined property placements configurations for the symbol. Each of the predefined configuration is represented by a name visible in the GUI and an ID that may be used to select a specific configuration. |
| Public Property | [DefaultScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~DefaultScheme.html) | Property to get or set a custom property placement scheme (property arrangement) as default one. Once set, the defined property arrangement applies wherever the symbol is used. |
| Public Property | [Selected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~Selected.html) | Gets a PropertyPlacementsSchema object that represents the selected property placements configuration. Sets the current property placements configuration. Note: Changing the current property placements configuration deletes the existing property placements. This can make some API objects of type PropertyPlacement become invalid. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Add](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~Add.html) | Adds or saves element representing property placements configuration for the symbol. This also sets the current property placements configuration of the symbol. |
| Public Method | [Export](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~Export.html) | Overloaded. Exports all the customer property placements sets of the symbol to a file. |
| Public Method | [Import](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~Import.html) | Imports customer property placements set(s) from the specified file to the symbol. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~Remove.html) | Removes a PropertyPlacementsSchema object that represents the property placements configuration. |


