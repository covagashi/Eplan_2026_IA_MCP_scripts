# ARTICLE_CREEPAGEDISTANCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CREEPAGEDISTANCE().html

---

Plugs: Creepage distance # 22097.

Syntax

**C#**



public MDPropertyValue ARTICLE_CREEPAGEDISTANCE {get; set;}

public:

property MDPropertyValue^ ARTICLE_CREEPAGEDISTANCE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. The creepage distance is defined as the shortest distance along the surface of an insulator between two conducting parts. This insulation does not depend on the length of voltage load.
