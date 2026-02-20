# FUNC_TERMINAL_IS_OPEN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINAL_IS_OPEN().html

---

Terminal opened # 20232.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_IS_OPEN {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_IS_OPEN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Indicates whether the terminal is opened. If the property is activated, the connection between the internal and external sides of the terminal is separated, i.e., the potential transfer within the terminal is interrupted. This property is available in terminal reports, where it can be used to output terminal graphics. You can show the state of an isolating terminal in this way, for example.
