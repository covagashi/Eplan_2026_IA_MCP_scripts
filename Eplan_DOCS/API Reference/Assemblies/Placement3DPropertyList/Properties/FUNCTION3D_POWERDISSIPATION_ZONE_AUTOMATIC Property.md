# FUNCTION3D_POWERDISSIPATION_ZONE_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic660.html

---

Thermal design: Air-conditioning field (automatic) # 36046.

Syntax

**C#**



public PropertyValue FUNCTION3D_POWERDISSIPATION_ZONE_AUTOMATIC {get; set;}

public:

property PropertyValue^ FUNCTION3D_POWERDISSIPATION_ZONE_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Number of the air-conditioning field (1 to 100). Is required for calculating the power dissipation.
