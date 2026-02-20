# FUNC_ARTICLE_APPARENT_POWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_APPARENT_POWER(Int32).html

---

Apparent power # 26550.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_APPARENT_POWER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_APPARENT_POWER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Total power available in an AC circuit. It is composed of the active power and the reactive power. The apparent power is measured in volt amperes (VA) and is obtained as the product of the root mean square value of the electric voltage and the root mean square value of the electric amperage.
