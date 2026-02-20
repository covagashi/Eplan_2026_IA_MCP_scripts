# ARTICLE_ENERGY_EFFICIENCY_CLASS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_ENERGY_EFFICIENCY_CLASS().html

---

Energy efficiency class # 26301.

Syntax

**C#**



public MDPropertyValue ARTICLE_ENERGY_EFFICIENCY_CLASS {get; set;}

public:

property MDPropertyValue^ ARTICLE_ENERGY_EFFICIENCY_CLASS {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Assessment scale that shows how much energy an electrical device uses compared to other devices. The energy efficiency class can be determined, for example, in accordance with the EU-wide standard method "Energy Label Classification" and can be specified in the graduations A to G.
