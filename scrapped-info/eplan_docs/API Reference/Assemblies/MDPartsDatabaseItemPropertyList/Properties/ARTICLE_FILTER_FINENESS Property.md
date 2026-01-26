# ARTICLE_FILTER_FINENESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FILTER_FINENESS().html

---

Grade of filtration # 26586.

Syntax

**C#**



public MDPropertyValue ARTICLE_FILTER_FINENESS {get; set;}

public:

property MDPropertyValue^ ARTICLE_FILTER_FINENESS {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Ability of a filter to retain particles of a certain size. The value is given in micrometers (µm) and indicates the maximum diameter of particles and suspended matter which are just let through by a filter irrespective of the type of filter material.
