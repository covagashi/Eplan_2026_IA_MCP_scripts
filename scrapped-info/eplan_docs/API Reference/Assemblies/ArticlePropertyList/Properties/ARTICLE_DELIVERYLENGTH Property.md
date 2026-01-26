# ARTICLE_DELIVERYLENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DELIVERYLENGTH().html

---

Delivery length # 22058.

Syntax

**C#**



public PropertyValue ARTICLE_DELIVERYLENGTH {get; set;}

public:

property PropertyValue^ ARTICLE_DELIVERYLENGTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Delivery length of the parts. During a part selection or device selection the property is filled with the corresponding value of the delivery length from the parts management. You can use the property in forms for the parts list, for example in calculation formulas for calculating the order length.
