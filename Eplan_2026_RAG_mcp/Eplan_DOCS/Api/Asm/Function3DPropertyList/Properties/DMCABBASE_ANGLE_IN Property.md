# DMCABBASE_ANGLE_IN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3DPropertyList~DMCABBASE_ANGLE_IN().html

---

Thermal design: Intake angle # 36461.

Syntax

**C#**



public PropertyValue DMCABBASE_ANGLE_IN {get; set;}

public:

property PropertyValue^ DMCABBASE_ANGLE_IN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Area parameter for calculating the optimally air-conditioned area (area that an air-conditioning unit can reliably air-condition on the basis of its air circulation capacity). Describes the width of the angle in which the air to be cooled / heated can enter the cooling device. Amounts uniformly to 60° for all devices.
