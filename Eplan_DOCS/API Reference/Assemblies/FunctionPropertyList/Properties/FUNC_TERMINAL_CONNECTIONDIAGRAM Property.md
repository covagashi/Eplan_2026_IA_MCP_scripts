# FUNC_TERMINAL_CONNECTIONDIAGRAM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINAL_CONNECTIONDIAGRAM().html

---

Terminal / plug connection diagram form # 20852.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_CONNECTIONDIAGRAM {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_CONNECTIONDIAGRAM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of the terminal or pin-connection diagram form to be used for reporting the terminal strip or plug.

If you assign a value using the API interface, please ensure that the relevant master data is available in the project.
