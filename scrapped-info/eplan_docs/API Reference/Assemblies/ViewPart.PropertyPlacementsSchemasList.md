# ViewPart.PropertyPlacementsSchemasList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart+PropertyPlacementsSchemasList.html

---

A structure representing a property placements schemas.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.ViewPart.PropertyPlacementsSchemasList**

Syntax

**C#**



public class ViewPart.PropertyPlacementsSchemasList

public ref class ViewPart.PropertyPlacementsSchemasList

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [All](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart+PropertyPlacementsSchemasList~All.html) | Returns an array of SymbolReference::PropertyPlacementsSchema elements representing predefined property placements configurations for the symbol. Each of the predefined configuration is represented by a name visible in the GUI and an ID that may be used to select a specific configuration. |
| Public Property | [Selected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart+PropertyPlacementsSchemasList~Selected.html) | Gets a PropertyPlacementsSchema object that represents the selected property placements configuration. Sets the current property placements configuration. Note: Changing the current property placements configuration deletes the existing property placements. This can make some API objects of type PropertyPlacement become invalid. |


