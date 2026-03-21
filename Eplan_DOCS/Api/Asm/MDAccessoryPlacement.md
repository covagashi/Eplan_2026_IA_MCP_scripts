# MDAccessoryPlacement

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacement.html

---

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)  
         **Eplan.EplApi.MasterData.MDAccessoryPlacement**

Syntax

**C#**



public class MDAccessoryPlacement : MDPartsDatabaseItem

public ref class MDAccessoryPlacement : public MDPartsDatabaseItem

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AccessoryPlacementPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacement~AccessoryPlacementPositions.html) | Get all accessory-placement positions that belongs to the accessory placement. |
| Public Property | [AdoId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~AdoId.html) | Gets a unique identifier in the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Database](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Database.html) | Gets the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Name](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacement~Name.html) | Returns the name of the accessoryplacement. |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Properties.html) | .NET Property enabling access to P8 properties of the PartsDatabaseItem object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacement~Type.html) | Overridden. Returns the part type of the part. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddAccessoryPlacementPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacement~AddAccessoryPlacementPosition.html) | Add a new accessory placement position to the part. That accessory placement position is added to the end of the accessory placement position list. |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDAccessoryPlacement object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [GetTimeStampOfLastChange](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetTimeStampOfLastChange.html) | Gets the TimeStamp of the last change from a DatabaseItem (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Method | [RemoveAccessoryPlacementPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacement~RemoveAccessoryPlacementPosition.html) | Removes the given AccessoryPlacement position from the part. |
| Public Method | [ToDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html) | Returns data model identifier which identifies this object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |


