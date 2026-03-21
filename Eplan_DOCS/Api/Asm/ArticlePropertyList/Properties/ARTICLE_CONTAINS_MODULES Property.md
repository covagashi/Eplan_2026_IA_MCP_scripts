# ARTICLE_CONTAINS_MODULES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTAINS_MODULES().html

---

Contains modules # 22424.

Syntax

**C#**



public PropertyValue ARTICLE_CONTAINS_MODULES {get; set;}

public:

property PropertyValue^ ARTICLE_CONTAINS_MODULES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows information on nested assemblies or modules. If an assembly or a module contains further assemblies and/or modules, the fact whether these elements contain further modules is indicated here.
