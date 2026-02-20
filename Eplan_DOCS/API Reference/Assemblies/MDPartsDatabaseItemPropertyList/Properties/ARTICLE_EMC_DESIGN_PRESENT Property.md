# ARTICLE_EMC_DESIGN_PRESENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_EMC_DESIGN_PRESENT().html

---

EMC version available # 26298.

Syntax

**C#**



public MDPropertyValue ARTICLE_EMC_DESIGN_PRESENT {get; set;}

public:

property MDPropertyValue^ ARTICLE_EMC_DESIGN_PRESENT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Specifies whether a product is designed to meet the requirements for electromagnetic compatibility (EMC). This means that the product is designed in such a way that it does not cause electromagnetic interference and is itself insensitive to such interference.
