# FUNC_PLCCHANNEL_DESIGNATION_CALCULATED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCHANNEL_DESIGNATION_CALCULATED().html

---

Channel designation (determined) # 20436.

Syntax

**C#**



public PropertyValue FUNC_PLCCHANNEL_DESIGNATION_CALCULATED {get; set;}

public:

property PropertyValue^ FUNC_PLCCHANNEL_DESIGNATION_CALCULATED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

PLC channel designation for PLC connection points and channels. The channel designation can be manually or automatically assigned. A channel must be unique within a PLC card. For power supply connection points, the assignment is usually graphical.
