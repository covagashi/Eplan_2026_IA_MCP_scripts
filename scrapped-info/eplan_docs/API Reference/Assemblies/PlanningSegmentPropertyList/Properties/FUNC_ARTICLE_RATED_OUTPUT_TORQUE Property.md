# FUNC_ARTICLE_RATED_OUTPUT_TORQUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1019.html

---

Nominal power # 26475.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_POWER_KW( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_POWER_KW {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Power of the device, which is specified by the manufacturer. The nominal power can relate to the power consumed or output, depending on the device.
