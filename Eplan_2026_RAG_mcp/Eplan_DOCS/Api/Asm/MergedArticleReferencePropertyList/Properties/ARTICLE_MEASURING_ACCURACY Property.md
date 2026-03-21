# ARTICLE_MEASURING_ACCURACY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_MEASURING_ACCURACY().html

---

Measurement accuracy # 26458.

Syntax

**C#**



public PropertyValue ARTICLE_MEASURING_ACCURACY {get; set;}

public:

property PropertyValue^ ARTICLE_MEASURING_ACCURACY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Degree of similarity between the result of a measurement and a true value of the quantity to be measured. Example: Digital multimeters often have an accuracy of ±0.5% to ±1% of the measured value. Pressure sensors often have an accuracy of ±0.1% to ±1% of the full scale range.
