# MDConstruction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConstruction.html

---

When a part will be fixed on a mounting panel, several holes are nessesary. The definition how to drill that holes is represented by a MDConstruction object

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)  
         **Eplan.EplApi.MasterData.MDConstruction**

Syntax

**C#**



public class MDConstruction : MDPartsDatabaseItem

public ref class MDConstruction : public MDPartsDatabaseItem


Remarks

To use that construction on a MDPart object, set the property ARTICLE\_REF\_CONSTRUCTION\_NAME to the name of the referenced construction

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdoId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~AdoId.html) | Gets a unique identifier in the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Database](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Database.html) | Gets the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [DrillingPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConstruction~DrillingPositions.html) | Get all drilling positions that belongs to the construction. |
| Public Property | [Name](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConstruction~Name.html) | Returns the name of the construction. |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Properties.html) | .NET Property enabling access to P8 properties of the PartsDatabaseItem object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConstruction~Type.html) | Overridden. Returns the part type of the part. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddDrillingPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConstruction~AddDrillingPosition.html) | Add a new drilling position to the part. That drilling position is added to the end of the drilling position list. |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDConstruction object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [GetTimeStampOfLastChange](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetTimeStampOfLastChange.html) | Gets the TimeStamp of the last change from a DatabaseItem (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Method | [RemoveDrillingPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConstruction~RemoveDrillingPosition.html) | Removes the given drilling position from the part. |
| Public Method | [ToDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html) | Returns data model identifier which identifies this object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |


