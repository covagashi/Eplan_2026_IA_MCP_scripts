# FUNC_DEVICETAG_FULLNAME_WITHSEPARATOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_FULLNAME_WITHSEPARATOR().html

---

Name (without project structures, with preceding sign) # 20214.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_FULLNAME_WITHSEPARATOR {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_FULLNAME_WITHSEPARATOR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the full name of a function without the project structures, but with information about the preceding sign.

Example: "U1-X1" is output for a terminal strip "=A+O-U1-X1" and "X2:3" is output for a terminal "=A-X2:3".
