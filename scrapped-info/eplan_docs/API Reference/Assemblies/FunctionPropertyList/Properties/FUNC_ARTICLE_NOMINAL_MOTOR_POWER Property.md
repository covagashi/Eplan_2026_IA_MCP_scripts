# FUNC_ARTICLE_NOMINAL_MOTOR_POWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_NOMINAL_MOTOR_POWER(Int32).html

---

Motor nominal power # 26463.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_MOTOR_POWER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_MOTOR_POWER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum power of the drive unit that can be achieved in continuous operation.
