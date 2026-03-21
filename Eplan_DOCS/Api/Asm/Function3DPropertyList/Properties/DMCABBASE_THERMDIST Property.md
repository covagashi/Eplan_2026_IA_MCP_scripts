# DMCABBASE_THERMDIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3DPropertyList~DMCABBASE_THERMDIST().html

---

Thermal design: Maximum reach # 36460.

Syntax

**C#**



public PropertyValue DMCABBASE_THERMDIST {get; set;}

public:

property PropertyValue^ DMCABBASE_THERMDIST {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Area parameter for calculating the optimally air-conditioned area (area that an air-conditioning unit can reliably air-condition on the basis of its air circulation capacity). Describes the distance in meters at which the flow speed of the emitted air drops below a value of 0.5 m/s.
