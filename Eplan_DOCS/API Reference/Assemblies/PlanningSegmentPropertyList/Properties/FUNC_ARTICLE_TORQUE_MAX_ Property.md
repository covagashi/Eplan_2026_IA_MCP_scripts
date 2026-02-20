# FUNC_ARTICLE_TORQUE_MAX_ Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_TORQUE_MAX_(Int32).html

---

Torque, max. # 26254.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TORQUE_MAX_( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TORQUE_MAX_ {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum mechanically permissible torque that the motor can output to the output shaft.
