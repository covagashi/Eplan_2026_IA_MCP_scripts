# FUNC_ARTICLE_INTAKE_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_INTAKE_CAPACITY(Int32).html

---

Intake capacity # 26195.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_INTAKE_CAPACITY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_INTAKE_CAPACITY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The ability of a system to draw in a certain amount of air or gas per unit of time. The value is given in cubic meters per hour (m³/h).
