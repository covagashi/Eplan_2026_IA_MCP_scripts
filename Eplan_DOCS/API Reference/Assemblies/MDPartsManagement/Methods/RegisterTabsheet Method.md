# RegisterTabsheet Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~RegisterTabsheet.html

---

Registers an additional tab sheet for the given item type.

Syntax

**C#**



public bool RegisterTabsheet( 

   string addinName,

   string itemType,

   string tabsheetName

)

public:

bool RegisterTabsheet( 

   String^ addinName,

   String^ itemType,

   String^ tabsheetName

)


#### Parameters

*addinName*


*itemType*
:   That item type can be a new one - registerd be RegisterItem(). Or it can be the standard eplan part item. Than use "eplan.part" for itemType.

*tabsheetName*
:   The dialog that will be shown when selection a item of type itemType. That dialog has to be a XAML-Dialog.
