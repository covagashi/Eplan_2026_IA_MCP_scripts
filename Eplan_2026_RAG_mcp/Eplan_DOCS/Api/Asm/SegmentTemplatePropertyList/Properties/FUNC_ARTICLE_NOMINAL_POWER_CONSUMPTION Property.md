# FUNC_ARTICLE_NOMINAL_POWER_CONSUMPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1186.html

---

Nominal power requirement # 26485.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_POWER_REQUIREMENT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_POWER_REQUIREMENT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum electrical power that a device or plant requires under normal operating conditions to function properly. This power is usually specified in kilowatts (kW).
