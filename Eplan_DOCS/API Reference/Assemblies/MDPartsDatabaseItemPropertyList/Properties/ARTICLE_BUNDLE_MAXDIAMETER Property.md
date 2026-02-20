# ARTICLE_BUNDLE_MAXDIAMETER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_BUNDLE_MAXDIAMETER().html

---

Maximum bundle diameter # 22259.

Syntax

**C#**



public MDPropertyValue ARTICLE_BUNDLE_MAXDIAMETER {get; set;}

public:

property MDPropertyValue^ ARTICLE_BUNDLE_MAXDIAMETER {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

The maximum bundle diameter indicates the maximum diameter of a bundle of connections that must be met in order to bundle it with this part (e.g., a cable tie or spiral coiled tube).
