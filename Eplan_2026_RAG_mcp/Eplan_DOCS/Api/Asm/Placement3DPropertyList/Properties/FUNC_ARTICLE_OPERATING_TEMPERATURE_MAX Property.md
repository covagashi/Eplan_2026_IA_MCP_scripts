# FUNC_ARTICLE_OPERATING_TEMPERATURE_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic562.html

---

Operating temperature, max. # 26240.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_OPERATING_TEMPERATURE_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_OPERATING_TEMPERATURE_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum temperature at which a device can be operated safely and reliably.
