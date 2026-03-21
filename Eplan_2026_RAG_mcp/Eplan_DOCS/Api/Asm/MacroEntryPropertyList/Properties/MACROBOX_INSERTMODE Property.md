# MACROBOX_INSERTMODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_INSERTMODE().html

---

Macro: Also insert macro box # 23013.

Syntax

**C#**



public PropertyValue MACROBOX_INSERTMODE {get; set;}

public:

property PropertyValue^ MACROBOX_INSERTMODE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies the behavior of the macro box during insertion of the associated macro.

0 = From project settings: The macro box is also inserted when the project setting "Also insert macro boxes" is activated.

1 = Yes: The macro box is always inserted.

2 = No: The macro box is never inserted.
