# ARTICLE_MAINTENANCE_CYCLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_MAINTENANCE_CYCLE().html

---

Maintenance cycle # 26637.

Syntax

**C#**



public PropertyValue ARTICLE_MAINTENANCE_CYCLE {get; set;}

public:

property PropertyValue^ ARTICLE_MAINTENANCE_CYCLE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Describes the entire sequence of maintenance activities that must be performed within a specific time period or after a specific number of hours of operation. A maintenance cycle can include multiple maintenance intervals and ensures that all necessary maintenance work is performed over time.
