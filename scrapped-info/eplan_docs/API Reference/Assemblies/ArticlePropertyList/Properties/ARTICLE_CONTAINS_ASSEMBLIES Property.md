# ARTICLE_CONTAINS_ASSEMBLIES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTAINS_ASSEMBLIES().html

---

Contains assemblies # 22425.

Syntax

**C#**



public PropertyValue ARTICLE_CONTAINS_ASSEMBLIES {get; set;}

public:

property PropertyValue^ ARTICLE_CONTAINS_ASSEMBLIES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows information on nested assemblies or modules. If an assembly or a module contains further assemblies and/or modules, the fact whether these elements contain further assemblies is indicated here.
