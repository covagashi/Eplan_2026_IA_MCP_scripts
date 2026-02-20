# FUNC_TERMINAL_STRIP_ALLOW_SAME_NAME_IN_MULTILEVEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic646.html

---

Terminal strips: Allow same designations within multi-level terminals # 20290.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_STRIP_ALLOW_SAME_NAME_IN_MULTILEVEL {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_STRIP_ALLOW_SAME_NAME_IN_MULTILEVEL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is used to specify whether a terminal designation within multi-level terminal may occur several times. In other words, several levels may have the same terminal designation. If the property is deactivated, the terminal designation must be unique for each level.
