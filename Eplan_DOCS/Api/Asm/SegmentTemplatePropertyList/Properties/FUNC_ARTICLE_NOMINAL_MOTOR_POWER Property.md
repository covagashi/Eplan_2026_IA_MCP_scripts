# FUNC_ARTICLE_NOMINAL_MOTOR_POWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1185.html

---

Nominal power consumption # 26483.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_POWER_CONSUMPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_POWER_CONSUMPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum electrical power consumed by a device or component under normal operating conditions. This power is usually specified in watts (W) or kilowatts (kW).
