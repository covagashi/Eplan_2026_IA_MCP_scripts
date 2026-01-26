# FUNC_SINGLE_LINE_FUNCTION_COUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_SINGLE_LINE_FUNCTION_COUNT().html

---

Number of functions # 20110.

Syntax

**C#**



public PropertyValue FUNC_SINGLE_LINE_FUNCTION_COUNT {get; set;}

public:

property PropertyValue^ FUNC_SINGLE_LINE_FUNCTION_COUNT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

You can use this property to show the number of connections on connection definition points (and functions). The entered value is placed in the schematic together with the connection definition point - usually represented as a forward slash. Values such as "3+PE" are permitted.
