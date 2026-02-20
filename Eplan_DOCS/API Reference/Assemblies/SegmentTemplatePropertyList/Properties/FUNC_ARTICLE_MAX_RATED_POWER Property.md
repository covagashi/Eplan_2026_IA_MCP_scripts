# FUNC_ARTICLE_MAX_RATED_POWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1181.html

---

Measurand # 26461.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MEASURED_VARIABLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MEASURED_VARIABLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Physical quantity or characteristic detected by a measuring instrument or sensor. This can be, for example, temperature, pressure, length, volume, mass or another measurable property. The measurand thus defines exactly what is measured.
