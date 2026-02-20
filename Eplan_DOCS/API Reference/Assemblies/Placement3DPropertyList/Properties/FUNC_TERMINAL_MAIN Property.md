# FUNC_TERMINAL_MAIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINAL_MAIN().html

---

Main terminal # 20220.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_MAIN {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_MAIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Defines a terminal as the main terminal; the terminal is then similar to a main function. For example, for a main terminal the function templates are displayed in the terminal strip navigator, and a device selection can be performed. A terminal strip can contain as many main terminals as you want.
