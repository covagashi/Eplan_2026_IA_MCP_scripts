# FUNC_TERMINAL_STRIP_DONT_USE_MAINTERMINAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINAL_STRIP_DONT_USE_MAINTERMINAL().html

---

Do not use main terminals # 20229.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_STRIP_DONT_USE_MAINTERMINAL {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_STRIP_DONT_USE_MAINTERMINAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is enabled for a terminal strip definition, the main terminals are handled in the same way as "normal" terminals. In this case, the terminal strip is not split into independent areas and is only defined via the terminal strip definition.
