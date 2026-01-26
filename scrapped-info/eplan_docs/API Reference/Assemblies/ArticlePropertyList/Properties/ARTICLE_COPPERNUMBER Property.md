# ARTICLE_COPPERNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_COPPERNUMBER().html

---

Copper weight # 22066.

Syntax

**C#**



public PropertyValue ARTICLE_COPPERNUMBER {get; set;}

public:

property PropertyValue^ ARTICLE_COPPERNUMBER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Specifies the proportion of copper in the cable. Since copper is calculated on the current daily value, the copper price is calculated separately from the costs of manufacture of the cable and added to the cable price. In order to avoid minute numerical values, the unit kg/km is used for the entry, for example 33.

The following formula can be used to calculate how high the copper price is:

For 100 m cable: Copper weight\*(CU-notation - Basic official price)/1000

Example: Copper surcharge for the cable (N)YM(ST)-J5x1,5/1,5, Basic official price: 300, Day official price: 425

Calculation: 7.7 \* (425 - 300)/1000 = EUR 0.96 CU surcharge (for 100 m)
