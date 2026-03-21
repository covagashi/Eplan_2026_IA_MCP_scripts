# MDComponentTemplatePosition

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition.html

---

Class represents function template of part which type = component.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData.html)  
      [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)  
         **Eplan.EplApi.MasterData.MDComponentTemplatePosition**

Syntax

**C#**



public class MDComponentTemplatePosition : MDFunctionTemplatePosition

public ref class MDComponentTemplatePosition : public MDFunctionTemplatePosition


Remarks

There are specialized classes to manipulate function template properties for parts with product group = electrical terminal, electrical plug, electrical relay, electrical PLC, cable, wire.

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdditionalDescription](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~AdditionalDescription.html) | Refers to the Description column in GUI. (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |
| Public Property | [Characteristic](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~Characteristic.html) | The characteristic of component template |
| Public Property | [ConnectionDimension](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~ConnectionDimension.html) | The connection dimension of component template |
| Public Property | [ConnectionPointCrossSection](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~ConnectionPointCrossSection.html) | The connection point cross-section of component template |
| Public Property | [ConnectionPointDescription](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~ConnectionPointDescription.html) | The connection point description of component template |
| Public Property | [ConnectionPointDesignation](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~ConnectionPointDesignation.html) | The connection point designation of component template |
| Public Property | [ContactIndex](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~ContactIndex.html) | The contact / coil index of the component template |
| Public Property | [FunctionDefinitionCategory](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~FunctionDefinitionCategory.html) | The category of the function definition set to the function template (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |
| Public Property | [FunctionDefinitionGroup](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~FunctionDefinitionGroup.html) | The group of the function definition set to the function template (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |
| Public Property | [FunctionDefinitionId](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~FunctionDefinitionId.html) | The id of the function definition set to the function template (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |
| Public Property | [HarnessLink](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~HarnessLink.html) | The link to master data in Harness proD (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |
| Public Property | [IsIntrinsicallySafe](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~IsIntrinsicallySafe.html) | Is component template intrinsically safe (yes / no) |
| Public Property | [IsRelevantToSafety](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~IsRelevantToSafety.html) | Is component template relevant to safety (yes / no) |
| Public Property | [PlugDeviceTag](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~PlugDeviceTag.html) | The plug device tag of component template |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~Properties.html) | (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |
| Public Property | [SummedUp](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~SummedUp.html) | Returns TRUE if the function template is part of an assembly or module and is summed up (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |
| Public Property | [Symbol](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~Symbol.html) | The symbol of component template |
| Public Property | [SymbolMacro](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDComponentTemplatePosition~SymbolMacro.html) | The symbol macro of component template |
| Public Property | [TemplateGroup](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~TemplateGroup.html) | The template group of the function template (Inherited from [Eplan.EplApi.MasterData.MDFunctionTemplatePosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData~Dispose().html) | Destructor for deterministic finalization of MDComponentTemplatePosition object. (Inherited from [Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemChildData.html)) |


