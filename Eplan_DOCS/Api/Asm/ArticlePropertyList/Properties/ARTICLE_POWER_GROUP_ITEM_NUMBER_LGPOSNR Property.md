# ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR().html

---

Performance description, standardized: Performance group item number # 26431.

Syntax

**C#**



public PropertyValue ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR {get; set;}

public:

property PropertyValue^ ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Unique identification number for a specific service item within a service group in the bill of quantities. Each service group contains several service items that can be identified by such a unique number. Example: In a performance group "Piping and support systems" a specific number stands for the position "Drilling through walls and ceilings made of masonry".
