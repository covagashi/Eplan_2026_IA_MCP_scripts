# ShowPartSelectionDialog(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowPartSelectionDialog(String,String).html

---

Select part from the current parts database

Syntax

**C#**



public bool ShowPartSelectionDialog( 

   ref string strPartNr,

   ref string strVariant

)

public:

bool ShowPartSelectionDialog( 

   String^% strPartNr,

   String^% strVariant

)


#### Parameters

*strPartNr*
:   The part number of the selected part. Can be set to preselect a part.

*strVariant*
:   The variant of the selected part. Can be set to preselect a part.

#### Return Value

TRUE, if a selection is committed successfully.

Remarks

Method ignores QuietMode and always shows dialog.
