# FUNC_ARTICLE_SET_POINT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_SET_POINT(Int32).html

---

Setpoint # 26568.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SET_POINT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SET_POINT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

In a closed loop control, this is the target value that the process value is to assume, expressed in units of the process value.
