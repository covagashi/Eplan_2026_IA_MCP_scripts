# FUNC_ARTICLE_NOMINAL_PRESSURE_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE_RANGE(Int32).html

---

Pressure range # 26473.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_PRESSURE_RANGE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_PRESSURE_RANGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specified graduation series in accordance with ISO 7268 for the maximum permissible working pressure.
