# ARTICLE_POWER_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_POWER_DESCRIPTION().html

---

Performance description (item, device) # 26427.

Syntax

**C#**



public PropertyValue ARTICLE_POWER_DESCRIPTION {get; set;}

public:

property PropertyValue^ ARTICLE_POWER_DESCRIPTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Describing texts or notes on an item or device. Example: The performance description of a motor can contain information about its maximum performance, rotation speed, efficiency class and operating areas.
