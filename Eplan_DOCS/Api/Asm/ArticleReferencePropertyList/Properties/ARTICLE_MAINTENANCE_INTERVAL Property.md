# ARTICLE_MAINTENANCE_INTERVAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_MAINTENANCE_INTERVAL().html

---

Maintenance interval # 26635.

Syntax

**C#**



public PropertyValue ARTICLE_MAINTENANCE_INTERVAL {get; set;}

public:

property PropertyValue^ ARTICLE_MAINTENANCE_INTERVAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specifies the period or operating hours between two maintenance tasks. Specification of how often a maintenance has to be carried out, for example every 6 months or every 500 operating hours.
