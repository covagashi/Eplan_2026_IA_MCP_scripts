# FUNC_ARTICLE_RATED_VOLTAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_VOLTAGE(Int32).html

---

Nominal voltage # 26487.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_VOLTAGE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_VOLTAGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The value of the voltage specified by the manufacturer or supplier in normal operation.
