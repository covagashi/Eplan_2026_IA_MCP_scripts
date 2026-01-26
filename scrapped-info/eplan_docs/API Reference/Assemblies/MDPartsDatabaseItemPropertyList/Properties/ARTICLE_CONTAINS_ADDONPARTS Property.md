# ARTICLE_CONTAINS_ADDONPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONTAINS_ADDONPARTS().html

---

Contains supplemental parts # 22423.

Syntax

**C#**



public MDPropertyValue ARTICLE_CONTAINS_ADDONPARTS {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONTAINS_ADDONPARTS {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows information on nested assemblies or modules. If an assembly or a module contains further assemblies and/or modules, the fact whether these elements contain supplemental parts is indicated here.
