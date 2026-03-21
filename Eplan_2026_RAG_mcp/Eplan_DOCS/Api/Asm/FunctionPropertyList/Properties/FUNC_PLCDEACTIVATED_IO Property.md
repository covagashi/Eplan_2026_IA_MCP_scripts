# FUNC_PLCDEACTIVATED_IO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCDEACTIVATED_IO().html

---

Deactivated I/O connection point # 20438.

Syntax

**C#**



public PropertyValue FUNC_PLCDEACTIVATED_IO {get; set;}

public:

property PropertyValue^ FUNC_PLCDEACTIVATED_IO {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Identifies a deactivated I/O connection point within a channel. A channel can have several I/O connection points, but only one of them can be active. Deactivated connection points are treated as power supplies. For example, when addressing a filled address, the address from the channel is overwritten.
