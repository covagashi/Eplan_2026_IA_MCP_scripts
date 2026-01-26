# FUNC_ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic952.html

---

Power consumption, max. # 26420.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MAX_POWER_CONSUMPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MAX_POWER_CONSUMPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum quantity of electrical energy that a device or component can consume during operation. The power consumption describes the actual energy consumption.
