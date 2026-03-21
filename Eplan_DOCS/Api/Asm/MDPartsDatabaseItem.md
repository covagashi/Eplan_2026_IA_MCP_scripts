# MDPartsDatabaseItem

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html

---

Base class of all items stored in parts database

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      **Eplan.EplApi.MasterData.MDPartsDatabaseItem**  
         [Eplan.EplApi.MasterData.MDAccessoryList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryList.html)  
         [Eplan.EplApi.MasterData.MDAccessoryPlacement](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacement.html)  
         [Eplan.EplApi.MasterData.MDAddress](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAddress.html)  
         [Eplan.EplApi.MasterData.MDConnectionPointInfo](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo.html)  
         [Eplan.EplApi.MasterData.MDConstruction](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConstruction.html)  
         [Eplan.EplApi.MasterData.MDPart](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart.html)

Syntax

**C#**



public class MDPartsDatabaseItem : PropertiesAndHandleObject

public ref class MDPartsDatabaseItem : public PropertiesAndHandleObject

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDPartsDatabaseItem Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~_ctor().html) | constructor of MDPartsDatabaseItem |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdoId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~AdoId.html) | Gets a unique identifier in the database, where the database item is stored |
| Public Property | [Database](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Database.html) | Gets the database, where the database item is stored |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Properties.html) | .NET Property enabling access to P8 properties of the PartsDatabaseItem object. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDPartsDatabaseItem object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Methodstatic (Shared in Visual Basic) | [FromDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~FromDataModelIdentifier.html) | Returns object found by its data model identifier. |
| Public Methodstatic (Shared in Visual Basic) | [GetAvailableProductGroups](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetAvailableProductGroups.html) | Gets all available product groups of a given product-top-group |
| Public Methodstatic (Shared in Visual Basic) | [GetAvailableProductSubGroups](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetAvailableProductSubGroups.html) | Gets all available product sub-groups of a given product-group |
| Public Methodstatic (Shared in Visual Basic) | [GetProductGroupName](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetProductGroupName.html) | Gets the name of the product-group |
| Public Methodstatic (Shared in Visual Basic) | [GetProductSubGroupName](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetProductSubGroupName.html) | Gets the name of the product-sub-group |
| Public Methodstatic (Shared in Visual Basic) | [GetProductTopGroupName](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetProductTopGroupName.html) | Gets the name of the product-top-group |
| Public Method | [GetTimeStampOfLastChange](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetTimeStampOfLastChange.html) | Gets the TimeStamp of the last change from a DatabaseItem |
| Public Method | [ToDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html) | Returns data model identifier which identifies this object. |


