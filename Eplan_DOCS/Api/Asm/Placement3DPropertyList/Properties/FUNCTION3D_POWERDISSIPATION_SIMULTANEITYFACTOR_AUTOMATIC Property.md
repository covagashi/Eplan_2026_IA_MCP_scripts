# FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic659.html

---

Thermal design: Simultaneity factor (automatic) # 36044.

Syntax

**C#**



public PropertyValue FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR_AUTOMATIC {get; set;}

public:

property PropertyValue^ FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only..

Is required for calculating the power dissipation. Displays the value of the simultaneity factor (if it exists). Otherwise the value from the project settings is used.
