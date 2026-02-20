# FUNC_TERMINAL_SWITCHABLE_JUMPER_EXTERN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINAL_SWITCHABLE_JUMPER_EXTERN().html

---

Switching jumper (external) # 20292.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_SWITCHABLE_JUMPER_EXTERN {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_SWITCHABLE_JUMPER_EXTERN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows the state of the switching jumper on the external side of the terminal:

0 = None,

1 = Open,

2 = Closed.

The "Closed" setting affects the logic (connections, potentials, etc.). If this setting has been selected for a terminal, a switching jumper connection to the next terminal will be created. The "Open" setting does not affect the logic; it only serves to recognize the switching state.
