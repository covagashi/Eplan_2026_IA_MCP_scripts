# FUNC_DISTRIBUTED_TERMINAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_DISTRIBUTED_TERMINAL().html

---

Distributed terminal # 20280.

Syntax

**C#**



public PropertyValue FUNC_DISTRIBUTED_TERMINAL {get; set;}

public:

property PropertyValue^ FUNC_DISTRIBUTED_TERMINAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Specifies whether a terminal is a distributed terminal. Terminal connection points can be shown distributed with the aid of distributed terminals. Each distributed terminal then represents one or several connection points of the terminal.
