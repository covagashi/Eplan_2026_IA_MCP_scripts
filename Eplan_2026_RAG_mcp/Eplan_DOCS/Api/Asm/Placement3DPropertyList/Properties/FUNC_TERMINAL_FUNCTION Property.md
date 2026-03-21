# FUNC_TERMINAL_FUNCTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINAL_FUNCTION().html

---

Terminal category # 20230.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_FUNCTION {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_FUNCTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property can be used to characterize a terminal precisely. The property is available in terminal reports, where it can be used to output terminal graphics. The following values are possible:

0 = Feed-through terminal,

1 = Isolating terminal,

2 = Switching terminal,

3 = Diode terminal,

4 = Fused terminal,

5 = Resistance terminal,

6 = Thermocouple terminal.
