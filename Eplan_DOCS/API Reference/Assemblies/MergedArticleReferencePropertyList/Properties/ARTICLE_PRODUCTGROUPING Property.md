# ARTICLE_PRODUCTGROUPING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_PRODUCTGROUPING().html

---

Product grouping # 22367.

Syntax

**C#**



public PropertyValue ARTICLE_PRODUCTGROUPING {get; set;}

public:

property PropertyValue^ ARTICLE_PRODUCTGROUPING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

In this property the classification of a part into "Generic product group", "Product group" and "Product subgroup" is made in the parts management in the tab "Properties" > Hierarchy level "General". The classification is displayed here like the directory path in a breadcrumb trail (e.g. "Electrical engineering > Cable > General").
