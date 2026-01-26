# FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic658.html

---

Thermal design: Simultaneity factor (device) # 36045.

Syntax

**C#**



public PropertyValue FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR {get; set;}

public:

property PropertyValue^ FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Deviating simultaneity factor for this device compared to the project properties. Is required for calculating the power dissipation.
