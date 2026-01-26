# FUNC_MAINCROSSREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_MAINCROSSREFERENCE().html

---

Cross-reference (only main functions) # 20306.

Syntax

**C#**



public PropertyValue FUNC_MAINCROSSREFERENCE {get; set;}

public:

property PropertyValue^ FUNC_MAINCROSSREFERENCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows cross-references for possible main functions of the device. The function category has to match here. This property can be used to show a cross-reference on a black box to the same black box placed elsewhere.
