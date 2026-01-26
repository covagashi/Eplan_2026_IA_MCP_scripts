# FUNC_DEVICETAG_NESTED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DEVICETAG_NESTED().html

---

DT (subordinate, without project structures) # 20004.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_NESTED {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_NESTED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Supplies the subordinate device tag without project structures.

Example: "K1" is output for "=A+O-U1-K1".
