# MDConnectionPointInfo

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo.html

---

This class represents connection points in the parts database. That connection points has a unique name (Name) and a list of connection terminals (MDConnectionPointPosition)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)  
         **Eplan.EplApi.MasterData.MDConnectionPointInfo**

Syntax

**C#**



public class MDConnectionPointInfo : MDPartsDatabaseItem

public ref class MDConnectionPointInfo : public MDPartsDatabaseItem


Remarks

To use that connection point info on a MDPart object, set the property ARTICLE\_REF\_TERMINAL\_NAME to the name of the referenced connection point info.

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdoId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~AdoId.html) | Gets a unique identifier in the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [ConnectionCategoryDefault](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~ConnectionCategoryDefault.html) | Standard connection category |
| Public Property | [ConnectionPointPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~ConnectionPointPositions.html) | Returns a list of connection terminals (MDConnectionPointPosition) They are ordered the same way as in parts management. |
| Public Property | [Database](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Database.html) | Gets the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Name](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~Name.html) | Returns the name of the connection point info. This name is the unique key. |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Properties.html) | .NET Property enabling access to P8 properties of the PartsDatabaseItem object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~Type.html) | Overridden. Returns the part type of the part. |
| Public Property | [WireTerminationProcessings](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~WireTerminationProcessings.html) | Returns a map of ids and theirs names of all possible wire termination processing. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddConnectionPointPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~AddConnectionPointPosition.html) | Adds a new connection terminal (MDConnectionPointPosition) to the connection point info. That position is added to the end of the connection point position list. |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDConnectionPointInfo object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [GetTimeStampOfLastChange](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetTimeStampOfLastChange.html) | Gets the TimeStamp of the last change from a DatabaseItem (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Method | [RemoveConnectionPointPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~RemoveConnectionPointPosition.html) | Removes the given connection point position from the connection point info. |
| Public Method | [ToDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html) | Returns data model identifier which identifies this object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |


