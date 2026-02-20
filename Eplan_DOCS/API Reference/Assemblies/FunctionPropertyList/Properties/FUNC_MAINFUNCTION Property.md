# FUNC_MAINFUNCTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_MAINFUNCTION().html

---

Main function # 20122.

Syntax

**C#**



public PropertyValue FUNC_MAINFUNCTION {get; set;}

public:

property PropertyValue^ FUNC_MAINFUNCTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Defines whether a function is a main function. The main function represents a device in the devices represented in a distributed manner (e.g. the coil in a contactor). Only the main function carries (e.g.) the device definition of the device.
