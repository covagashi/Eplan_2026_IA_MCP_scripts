# ARTICLE_MAX_RATED_CURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MAX_RATED_CURRENT().html

---

Nominal current, max. # 26500.

Syntax

**C#**



public MDPropertyValue ARTICLE_MAX_RATED_CURRENT {get; set;}

public:

property MDPropertyValue^ ARTICLE_MAX_RATED_CURRENT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum permissible current that an electrical device or a plant can carry continuously without overheating or damage occurring. This value is, among other things, decisive for the dimensioning of items and fuses.
