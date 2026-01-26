# FUNC_ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN(Int32).html

---

Actual power (pneumatic), min. # 26392.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Lowest pneumatic power output or consumption (product of the rated flow rate and pressure of a pressure fluid) of the item or system, determined in a defined time interval.
