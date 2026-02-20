# MDPart

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart.html

---

This class represents a part in the parts database. That part can be a component, assembly or module - depending on the Type (MDPartsDatabaseItem.Enums.Type)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)  
         **Eplan.EplApi.MasterData.MDPart**

Syntax

**C#**



public class MDPart : MDPartsDatabaseItem

public ref class MDPart : public MDPartsDatabaseItem

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AccessoryPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AccessoryPositions.html) | Get all accessory positions that belongs to the part |
| Public Property | [AdoId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~AdoId.html) | Gets a unique identifier in the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [AssemblyPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AssemblyPositions.html) | Get all Assembly positions of the part. |
| Public Property | [ConnectionPointInfo](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ConnectionPointInfo.html) | Get the connection point info associated with this part. |
| Public Property | [Database](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Database.html) | Gets the database, where the database item is stored (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [DoorPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~DoorPositions.html) | Get all DoorPosition that belongs to the part. |
| Public Property | [FunctionTemplatePositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~FunctionTemplatePositions.html) | Gets all FuctionTemplates as MDFunctionTemplatePosition object from the part. |
| Public Property | [GenericProductGroup](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~GenericProductGroup.html) | Gets/Sets the generic product group of the part. |
| Public Property | [LockedMountingAreaPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~LockedMountingAreaPositions.html) | Get all locked mounting area positions of the part. |
| Public Property | [ModulePositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ModulePositions.html) | Get all Module positions of the part. |
| Public Property | [MountingPanelPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~MountingPanelPositions.html) | Get all support mounting panel positions of the part. |
| Public Property | [PartConstructionPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~PartConstructionPositions.html) | Get all part construction panel positions of the part. |
| Public Property | [PartNr](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~PartNr.html) | Returns the part number of the part. |
| Public Property | [ProductGroup](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ProductGroup.html) | Gets/Sets the product group of the part. |
| Public Property | [ProductSubGroup](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ProductSubGroup.html) | Gets/Sets the product sub group of the part. |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~Properties.html) | .NET Property enabling access to P8 properties of the PartsDatabaseItem object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Property | [SafetyRelatedValuePositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~SafetyRelatedValuePositions.html) | Get all safety related valud positions of the part. |
| Public Property | [SupportBarPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~SupportBarPositions.html) | Get all support bar area positions of the part. |
| Public Property | [SymbolPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~SymbolPositions.html) | Get all symbol positions assigned to the part. |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~Type.html) | Overridden. Returns the part type of the part. |
| Public Property | [UserDefinedPropertyPositions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~UserDefinedPropertyPositions.html) | Gets all user defined property positions |
| Public Property | [Variant](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~Variant.html) | Returns the variant of the part. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddAccessoryPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddAccessoryPosition.html) | Add a new accessory position to the part. That new accessory part is added to the end of the accessory position list. |
| Public Method | [AddAssemblyPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddAssemblyPosition.html) | Add a new assembly position to the part. That position is added to the end of the assembly position list. |
| Public Method | [AddDoorPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddDoorPosition.html) | Add a new DoorPosition to the part. That DoorPosition is added to the end of the DoorPossition list. |
| Public Method | [AddFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddFunctionTemplatePosition.html) | Overloaded. Adds a copy of FunctionTemplate to the part. |
| Public Method | [AddLockedMountingAreaPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddLockedMountingAreaPosition.html) | Add a new locked mounting area position to the part. That position is added to the end of the locked mounting area position list. |
| Public Method | [AddModulePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddModulePosition.html) | Add a new module position to the part. That position is added to the end of the module position list. |
| Public Method | [AddMountingPanelPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddMountingPanelPosition.html) | Add a new mounting panel position to the part. That position is added to the end of the mounting panel position list. |
| Public Method | [AddPartConstructionPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddPartConstructionPosition.html) | Add a new part construction position to the part. That position is added to the end of the part construction position list. |
| Public Method | [AddSafetyRelatedValuePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddSafetyRelatedValuePosition.html) | Add a new safety related value position to the part. That position is added to the end of the safety related value position list. |
| Public Method | [AddSupportBarPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddSupportBarPosition.html) | Add a new support bar position to the part. That position is added to the end of the support bar position list. |
| Public Method | [AddSymbolPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddSymbolPosition.html) | Add a new symbol position to the part. Symbol is added at the first available index of symbol position list. |
| Public Method | [AddUserDefinedPropertyPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddUserDefinedPropertyPosition.html) | Adds a new UserDefinedPropertyPosition object to the part. It is added to the end of the parts UserDefinedPropertyPositions list. |
| Public Method | [AssignConfigurablePropertiesScheme](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AssignConfigurablePropertiesScheme.html) | Assigns given configurable properties scheme to the part. |
| Public Method | [AssignFreePropertiesScheme](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AssignFreePropertiesScheme.html) | Assigns given free properties scheme to the part. |
| Public Method | [ChangeFunctionTemplateDefinition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ChangeFunctionTemplateDefinition.html) | Changes function definition of a function template position |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDPart object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [Duplicate](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~Duplicate.html) | Overloaded. Create a new part with identical data. That new part will get the given part number and variant |
| Public Method | [GetTimeStampOfLastChange](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~GetTimeStampOfLastChange.html) | Gets the TimeStamp of the last change from a DatabaseItem (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |
| Public Method | [RemoveAccessoryPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveAccessoryPosition.html) | Removes the given accessory position from the part. |
| Public Method | [RemoveAssemblyPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveAssemblyPosition.html) | Removes the given assembly position from the part. |
| Public Method | [RemoveDoorPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveDoorPosition.html) | Removes the given DoorPosition from the part. |
| Public Method | [RemoveFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveFunctionTemplatePosition.html) | Removes the given functionTemplate from the part |
| Public Method | [RemoveLockedMountingAreaPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveLockedMountingAreaPosition.html) | Removes the given locked mounting area position from the part. |
| Public Method | [RemoveModulePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveModulePosition.html) | Removes the given module position from the part. |
| Public Method | [RemoveMountingPanelPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveMountingPanelPosition.html) | Removes the given mounting panel position from the part. |
| Public Method | [RemovePartConstructionPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemovePartConstructionPosition.html) | Removes the given part construction position from the part. |
| Public Method | [RemoveSafetyRelatedValuePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveSafetyRelatedValuePosition.html) | Removes the given safety related value position from the part. |
| Public Method | [RemoveSupportBarPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveSupportBarPosition.html) | Removes the given support bar position from the part. |
| Public Method | [RemoveSymbolPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveSymbolPosition.html) | Removes the given symbol position from the part. |
| Public Method | [RemoveUserDefinedPropertyPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveUserDefinedPropertyPosition.html) | Removes the given UserDefinedPropertyPosition from a part. |
| Public Method | [SumUpFunctionTemplates](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~SumUpFunctionTemplates.html) | For assemblies and modules, sums up the function templates. This method works on this MDPart only and not recursively. All previous MDFunctionTemplatePositions of this MDPart will not be valid anymore. |
| Public Method | [ToDataModelIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem~ToDataModelIdentifier.html) | Returns data model identifier which identifies this object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItem.html)) |


