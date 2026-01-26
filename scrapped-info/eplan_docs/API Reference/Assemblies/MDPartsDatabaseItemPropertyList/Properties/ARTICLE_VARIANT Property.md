# ARTICLE_VARIANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_VARIANT().html

---

Variant # 22024.

Syntax

**C#**



public MDPropertyValue ARTICLE_VARIANT {get; set;}

public:

property MDPropertyValue^ ARTICLE_VARIANT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Shows the designation of the variant, up to 3 characters may be entered. A part always has at least one variant. By default, the variant designation "1" is assigned to the first variant of each part.
