# MDAccessoryListPosition

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryListPosition.html

---

MDAccessoryList objects can hold a list of accessory positions These are represented by a MDAccessoryListPosition object

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData.html)  
      **Eplan.EplApi.MasterData.MDAccessoryListPosition**

Syntax

**C#**



public class MDAccessoryListPosition : MDPartsDatabaseItemChildData

public ref class MDAccessoryListPosition : public MDPartsDatabaseItemChildData


Remarks

In order to get the value of readonly field Designation1, user have to get the corresponding part (using the partnr) and take the property: EW3\_PROPERTY\_ARTICLE\_DESCR1.

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AccessoryPlacement](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryListPosition~AccessoryPlacement.html) | Returns the accessory placement name. |
| Public Property | [PartNr](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryListPosition~PartNr.html) | Returns the part number of the referenced part. |
| Public Property | [Variant](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryListPosition~Variant.html) | Returns the part number of the referenced part. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData~Dispose().html) | Destructor for deterministic finalization of MDAccessoryListPosition object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData.html)) |


