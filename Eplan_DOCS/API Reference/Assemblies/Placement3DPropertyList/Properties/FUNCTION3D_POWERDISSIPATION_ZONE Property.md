# FUNCTION3D_POWERDISSIPATION_ZONE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_POWERDISSIPATION_ZONE().html

---

Thermal design: Air-conditioning field (device) # 36047.

Syntax

**C#**



public PropertyValue FUNCTION3D_POWERDISSIPATION_ZONE {get; set;}

public:

property PropertyValue^ FUNCTION3D_POWERDISSIPATION_ZONE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Deviating number of the air-conditioning field of this device from the number of the air-conditioning field of the enclosure (1 to 100). Is required for calculating the power dissipation.
