# ShowPartSelectionDialog(String,String,PartsDatabaseItemType) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowPartSelectionDialog(String,String,PartsDatabaseItemType).html

---

Select item from the current parts database

Syntax

**C#**



public bool ShowPartSelectionDialog( 

   ref string strPartNr,

   ref string strVariant,

   ref EplApplication.PartsDatabaseItemType nPartType

)

public:

bool ShowPartSelectionDialog( 

   String^% strPartNr,

   String^% strVariant,

   EplApplication.PartsDatabaseItemType% nPartType

)


#### Parameters

*strPartNr*
:   The part number or name of the selected item. Can be set to preselect an item.

*strVariant*
:   The variant of the selected item. Can be set to preselect a item (only used on parts).

*nPartType*
:   The type of the selected item. Can be set to preselect a item.

#### Return Value

TRUE, if a selection is committed successfully.

Remarks

Method ignores QuietMode and always shows dialog.
