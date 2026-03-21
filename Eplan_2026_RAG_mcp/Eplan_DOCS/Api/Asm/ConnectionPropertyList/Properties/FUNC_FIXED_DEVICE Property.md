# FUNC_FIXED_DEVICE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_FIXED_DEVICE().html

---

Device protection # 20475.

Syntax

**C#**



public PropertyValue FUNC_FIXED_DEVICE {get; set;}

public:

property PropertyValue^ FUNC_FIXED_DEVICE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Specifies whether a device protection is assigned to the function, connection or planning object. The assigned parts cannot be changed at a device / planning object with device protection. All the properties that are assigned through the part (and the function templates stored at the part) are thus protected.
