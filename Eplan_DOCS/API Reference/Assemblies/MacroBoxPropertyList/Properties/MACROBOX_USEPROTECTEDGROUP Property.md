# MACROBOX_USEPROTECTEDGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBoxPropertyList~MACROBOX_USEPROTECTEDGROUP().html

---

Macro: Protected group # 23012.

Syntax

**C#**



public PropertyValue MACROBOX_USEPROTECTEDGROUP {get; set;}

public:

property PropertyValue^ MACROBOX_USEPROTECTEDGROUP {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Determines at a macro box in a macro project that a protected group is created during the insertion of a macro. The inserted macro cannot be graphically changed or further broken down in the schematic project.
