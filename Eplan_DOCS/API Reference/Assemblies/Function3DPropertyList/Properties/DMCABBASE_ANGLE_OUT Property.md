# DMCABBASE_ANGLE_OUT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3DPropertyList~DMCABBASE_ANGLE_OUT().html

---

Thermal design: Discharge angle # 36462.

Syntax

**C#**



public PropertyValue DMCABBASE_ANGLE_OUT {get; set;}

public:

property PropertyValue^ DMCABBASE_ANGLE_OUT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Area parameter for calculating the optimally air-conditioned area (area that an air-conditioning unit can reliably air-condition on the basis of its air circulation capacity). Describes the width of the angle in which the cooled / heated air can exit the cooling device. Amounts uniformly to 60° for all devices.
