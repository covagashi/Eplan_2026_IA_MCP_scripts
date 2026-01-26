# FUNC_CABLE_ALLOW_TWO_SIDED_SHIELDINGS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLE_ALLOW_TWO_SIDED_SHIELDINGS().html

---

Allow shields connected on both sides # 20063.

Syntax

**C#**



public PropertyValue FUNC_CABLE_ALLOW_TWO_SIDED_SHIELDINGS {get; set;}

public:

property PropertyValue^ FUNC_CABLE_ALLOW_TWO_SIDED_SHIELDINGS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Suppresses the P003018 message "Shield applied too often" in the project check.
