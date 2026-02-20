# FUNC_ARTICLE_INITIAL_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1169.html

---

Frequency (input voltage) # 26341.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_INPUT_VOLTAGE_FREQUENCY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_INPUT_VOLTAGE_FREQUENCY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Frequency of the voltage supplied to a device or system.
