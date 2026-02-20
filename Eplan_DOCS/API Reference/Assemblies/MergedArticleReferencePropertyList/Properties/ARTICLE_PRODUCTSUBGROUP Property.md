# ARTICLE_PRODUCTSUBGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_PRODUCTSUBGROUP().html

---

Product subgroup # 22028.

Syntax

**C#**



public PropertyValue ARTICLE_PRODUCTSUBGROUP {get; set;}

public:

property PropertyValue^ ARTICLE_PRODUCTSUBGROUP {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Outputs the product subgroup entered in parts management on the "Properties" tab > hierarchy level "General" > "Product grouping" property. The parts are sorted according to their product groups (including superseding and subgroups) and displayed in tree format in parts management.
