# FUNC_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic526.html

---

Actual power (pneumatic), max. # 26390.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum pneumatic power output or consumption (product of rated flow rate and pressure of a pressure fluid) of the item or system, determined in a defined time interval.
