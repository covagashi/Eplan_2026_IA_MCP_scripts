# MDAddress

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAddress.html

---

Class for customer and manufacturer/supplier This class represents an address in the parts database. That address can be a customer or manufacturer/supplier - depending on the Type (MDPartsDatabaseItem.Enums.Type)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)  
         **Eplan.EplApi.MasterData.MDAddress**

Syntax

**C#**



public class MDAddress : MDPartsDatabaseItem

public ref class MDAddress : public MDPartsDatabaseItem

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdoId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~AdoId.html) | Gets a unique identifier in the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Database](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Database.html) | Gets the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Properties.html) | .NET Property enabling access to P8 properties of the PartsDatabaseItem object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [ShortName](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAddress~ShortName.html) | Returns the short name of the address. This short name combined with the Type of the address is the unique key. |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAddress~Type.html) | Overridden. Returns the part type of the part. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDAddress object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [GetTimeStampOfLastChange](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetTimeStampOfLastChange.html) | Gets the TimeStamp of the last change from a DatabaseItem (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Method | [ToDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html) | Returns data model identifier which identifies this object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |


