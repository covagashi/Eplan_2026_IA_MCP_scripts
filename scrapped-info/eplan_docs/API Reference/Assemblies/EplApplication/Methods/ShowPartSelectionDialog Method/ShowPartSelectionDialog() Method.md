# ShowPartSelectionDialog() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowPartSelectionDialog().html

---

Selects parts from the current parts database

Syntax

**C#**



public KeyValuePair<string,string>[] ShowPartSelectionDialog()

public:

array<KeyValuePair<String^,String^>>^ ShowPartSelectionDialog();


#### Return Value

NULL, if the selection was not committed with OK button. Otherwise, an array of string pairs where first string is a part number of a selected article and the second string is its variant name.

Remarks

Method ignores QuietMode and always shows dialog.
