# FUNC_ARTICLE_DUTY_CYCLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_DUTY_CYCLE(Int32).html

---

Duty cycle # 26294.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_DUTY_CYCLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_DUTY_CYCLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The ratio of the switch-on time to the total time for a predetermined time interval.
