# PROJECT_POWERDISSIPATION_SIMULTANEITYFACTOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_POWERDISSIPATION_SIMULTANEITYFACTOR().html

---

Thermal design: Simultaneity factor # 10312.

Syntax

**C#**



public PropertyValue PROJECT_POWERDISSIPATION_SIMULTANEITYFACTOR {get; set;}

public:

property PropertyValue^ PROJECT_POWERDISSIPATION_SIMULTANEITYFACTOR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Simultaneity factor for calculating the power dissipation. The simultaneity factor is an estimated value that takes into consideration the fact all the devices are never switched on simultaneously at full power in a plant.
