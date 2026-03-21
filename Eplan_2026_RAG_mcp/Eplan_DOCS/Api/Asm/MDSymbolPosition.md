# MDSymbolPosition

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition.html

---

Class represents symbol data stored in MDPart object.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDSymbolPosition**

Syntax

**C#**



public class MDSymbolPosition

public ref class MDSymbolPosition


Remarks

Symbol data which this object represents are stored in MDParts property list under property ARTICLE\_REPORT\_SYMBOL. Each not empty index of this property stores data of one symbol assigned to part. `RefPos` is the index under which data represented by this object are stored.

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [RefPos](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~RefPos.html) | Returns 1-based index of property ARTICLE\_REPORT\_SYMBOL under which data represented by this object are stored. |
| Public Property | [SymbolLibraryName](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~SymbolLibraryName.html) | Name of symbol library. |
| Public Property | [SymbolNumber](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~SymbolNumber.html) | Number identifying symbol in the symbol library. |
| Public Property | [SymbolVariantNr](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~SymbolVariantNr.html) | Number of symbol variant. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Methodstatic (Shared in Visual Basic) | [AddSymbolPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~AddSymbolPosition.html) | Add a new symbol position to part. Symbol is added at the first available index of symbol position list. |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~Dispose().html) | Destructor for deterministic finalization of MDSymbolPosition object. |
| Public Method | [RemoveSymbolPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~RemoveSymbolPosition.html) | Removes the symbol position from part. |


