# ReferencesActive Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~ReferencesActive.html

---

This property corresponds with the "Individual objects assignment" flag in the macro box dialog.

Syntax

**C#**



public bool ReferencesActive {get; set;}

public:

property bool ReferencesActive {

   bool get();

   void set (    bool value);

}


Remarks

If it is set to false then MacroBox should have associated all objects that are inside. If it is set to true, then MacroBox should have associated only objects that were "manually" set as associated
