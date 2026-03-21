# ARTICLE_CODING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CODING().html

---

Plugs: Coding # 22103.

Syntax

**C#**



public MDPropertyValue ARTICLE_CODING {get; set;}

public:

property MDPropertyValue^ ARTICLE_CODING {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Coding is required in order to distinguish between several plugs.
