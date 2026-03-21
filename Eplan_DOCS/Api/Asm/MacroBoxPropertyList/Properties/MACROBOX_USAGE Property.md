# MACROBOX_USAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBoxPropertyList~MACROBOX_USAGE().html

---

Macro: Type of usage # 23011.

Syntax

**C#**



public PropertyValue MACROBOX_USAGE {get; set;}

public:

property PropertyValue^ MACROBOX_USAGE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

The type of usage is used to differentiate macros in the macro navigator, and specifies which of the functionalities "Generate macros automatically" and "Update macros" can be executed and which not.

0 = Not specified: Generation and updating are possible.

1 = Defining: Is only taken into consideration for generating.

2 = Referencing: Is only taken into consideration for updating.

3 = Subordinate: Neither generating nor updating is possible.
