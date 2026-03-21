# FUNC_DEVICETAG_FULLNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_DEVICETAG_FULLNAME().html

---

Name (without project structures) # 20058.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_FULLNAME {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_FULLNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Specifies the full name of a function without the project structures.

Example: "U1-X1" is output for a terminal strip "=A+O-U1-X1" and "X2:3" is output for a terminal "=A-X2:3".
