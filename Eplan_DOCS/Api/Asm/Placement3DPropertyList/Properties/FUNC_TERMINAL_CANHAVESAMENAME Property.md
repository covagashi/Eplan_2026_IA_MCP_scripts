# FUNC_TERMINAL_CANHAVESAMENAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINAL_CANHAVESAMENAME().html

---

Allow same designations # 20811.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_CANHAVESAMENAME {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_CANHAVESAMENAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is used to specify whether a terminal designation within the terminal strip may occur several times. If you place the terminals in several representation types, you should not activate this setting and define each terminal uniquely. Otherwise there may be problems in global editing.
