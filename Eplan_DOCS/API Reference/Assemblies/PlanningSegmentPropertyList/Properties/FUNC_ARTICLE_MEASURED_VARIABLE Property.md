# FUNC_ARTICLE_MEASURED_VARIABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic956.html

---

Measurement accuracy # 26459.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MEASURING_ACCURACY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MEASURING_ACCURACY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Degree of similarity between the result of a measurement and a true value of the quantity to be measured. Example: Digital multimeters often have an accuracy of ±0.5% to ±1% of the measured value. Pressure sensors often have an accuracy of ±0.1% to ±1% of the full scale range.
