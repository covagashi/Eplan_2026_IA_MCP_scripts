# MDAccessoryPosition

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition.html

---

each part can store a list of accessories. Each accessory is represented with MDAccessoryPosition object That accessory can be a part (type = Component), than Name and Variant is used. Or a accessorylist (type = AccessoryList), than only Name is used. Type property is automatically set after Part or AccessoryList is correctly set

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData.html)  
      **Eplan.EplApi.MasterData.MDAccessoryPosition**

Syntax

**C#**



public class MDAccessoryPosition : MDPartsDatabaseItemChildData

public ref class MDAccessoryPosition : public MDPartsDatabaseItemChildData

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AccessoryList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~AccessoryList.html) | Returns the referenced AccessoryList if type is AccessoryList |
| Public Property | [AccessoryPlacement](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~AccessoryPlacement.html) | Returns the name of the accessory placement. |
| Public Property | [Designation1](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~Designation1.html) | Returns the Designation1 property from the corresponding part |
| Public Property | [Name](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~Name.html) | Returns the part number of the referenced part (if type is not AccessoryList). |
| Public Property | [Necessary](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~Necessary.html) | Returns wether the part / accessory list is neseccary. |
| Public Property | [Part](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~Part.html) | Returns the referenced part. |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~Type.html) | Returns the part type part / accessory list. It sets automatically after property Part or AccessoryList is correctly set |
| Public Property | [Variant](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPosition~Variant.html) | Returns the variant of the referenced part (if type is not AccessoryList). |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData~Dispose().html) | Destructor for deterministic finalization of MDAccessoryPosition object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData.html)) |


