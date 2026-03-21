# ARTICLE_CONTAINS_ASSEMBLIES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONTAINS_ASSEMBLIES().html

---

Contains assemblies # 22425.

Syntax

**C#**



public MDPropertyValue ARTICLE_CONTAINS_ASSEMBLIES {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONTAINS_ASSEMBLIES {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows information on nested assemblies or modules. If an assembly or a module contains further assemblies and/or modules, the fact whether these elements contain further assemblies is indicated here.
