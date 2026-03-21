# PROJECT_POWERDISSIPATION_POWER_OF_ZONE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_POWERDISSIPATION_POWER_OF_ZONE(Int32).html

---

Thermal design: Total power dissipation for air-conditioning field # 10313.

Syntax

**C#**



public PropertyValue PROJECT_POWERDISSIPATION_POWER_OF_ZONE( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJECT_POWERDISSIPATION_POWER_OF_ZONE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

Total power dissipation for air-conditioning fields, contains the calculation of the power dissipation.
