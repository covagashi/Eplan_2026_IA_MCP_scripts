# FUNC_DISTRIBUTED_TERMINAL_CROSSREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DISTRIBUTED_TERMINAL_CROSSREFERENCE().html

---

Distributed terminals cross-reference # 20252.

Syntax

**C#**



public PropertyValue FUNC_DISTRIBUTED_TERMINAL_CROSSREFERENCE {get; set;}

public:

property PropertyValue^ FUNC_DISTRIBUTED_TERMINAL_CROSSREFERENCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The distributed terminal's cross-reference refers from the first distributed terminal (according to the sequence in the terminal strip navigator and, primarily, the main terminal if one exists) to all other distributed terminals with the same terminal designation. For all other distributed terminals, this cross-reference refers back to the first distributed terminal.
