# FUNC_ARTICLE_NOMINAL_PRESSURE_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic963.html

---

Nominal pressure series # 26310.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_PRESSURE_SERIES( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_PRESSURE_SERIES {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Defined, agreed graduation series for maximum permissible working pressures.
