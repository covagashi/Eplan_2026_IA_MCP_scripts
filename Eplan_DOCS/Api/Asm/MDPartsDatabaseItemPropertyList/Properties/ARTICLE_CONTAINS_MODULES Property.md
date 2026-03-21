# ARTICLE_CONTAINS_MODULES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONTAINS_MODULES().html

---

Contains modules # 22424.

Syntax

**C#**



public MDPropertyValue ARTICLE_CONTAINS_MODULES {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONTAINS_MODULES {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows information on nested assemblies or modules. If an assembly or a module contains further assemblies and/or modules, the fact whether these elements contain further modules is indicated here.
