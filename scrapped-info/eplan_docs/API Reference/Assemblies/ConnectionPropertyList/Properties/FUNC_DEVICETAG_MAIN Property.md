# FUNC_DEVICETAG_MAIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETAG_MAIN().html

---

DT (superior, without project structures) # 20003.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_MAIN {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_MAIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Supplies the superior device tag without project structures.

Example: "U1" is output for "=A+O-U1-K1".
