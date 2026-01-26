# MDAccessoryList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryList.html

---

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)  
         **Eplan.EplApi.MasterData.MDAccessoryList**

Syntax

**C#**



public class MDAccessoryList : MDPartsDatabaseItem

public ref class MDAccessoryList : public MDPartsDatabaseItem

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AccessoryListPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryList~AccessoryListPositions.html) | Get all accessory positions that belongs to the accessory list. |
| Public Property | [AdoId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~AdoId.html) | Gets a unique identifier in the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Database](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Database.html) | Gets the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Name](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryList~Name.html) | Returns the name of the accessorylist. |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Properties.html) | .NET Property enabling access to P8 properties of the PartsDatabaseItem object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryList~Type.html) | Overridden. Returns the part type of the part. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddAccessoryListPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryList~AddAccessoryListPosition.html) | Add a new accessory list position to the part. That accessory list position is added to the end of the accessory list position list. |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDAccessoryList object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [GetTimeStampOfLastChange](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetTimeStampOfLastChange.html) | Gets the TimeStamp of the last change from a DatabaseItem (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Method | [RemoveAccessoryListPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryList~RemoveAccessoryListPosition.html) | Removes the given AccessoryList position from the part. |
| Public Method | [ToDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html) | Returns data model identifier which identifies this object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |


