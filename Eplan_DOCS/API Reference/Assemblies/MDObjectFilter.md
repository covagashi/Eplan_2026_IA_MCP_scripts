# MDObjectFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDObjectFilter.html

---

To filter objects by conditions, there is the class MDObjectFilter. Works like known from the filter-technique in the UI.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDObjectFilter**

Syntax

**C#**



public class MDObjectFilter

public ref class MDObjectFilter

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDObjectFilter Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDObjectFilter~_ctor.html) | Default constructor. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddLogicalOr](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDObjectFilter~AddLogicalOr.html) | Add a logical or - operator |
| Public Method | [AddPropertyCondition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDObjectFilter~AddPropertyCondition.html) | Add a property condition to the object filter. Adding multiple conditions without a separating OR-condition means, they must all match (logical AND-combination) |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDObjectFilter~Dispose().html) | Destructor for deterministic finalization of MDObjectFilterConditions object. |


