# ARTICLE_MODULE_POS_PLACE_SPREADED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MODULE_POS_PLACE_SPREADED().html

---

Distributed placement of module # 22288.

Syntax

**C#**



public PropertyValue ARTICLE_MODULE_POS_PLACE_SPREADED {get; set;}

public:

property PropertyValue^ ARTICLE_MODULE_POS_PLACE_SPREADED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Property of a part variant. Controls how a module is placed in Eplan Pro Panel:

0 = Place module parts and elements

1 = Place only module parts

2 = Place only elements
