# ARTICLE_DESIGN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_DESIGN().html

---

Plugs: Type of construction # 22100.

Syntax

**C#**



public MDPropertyValue ARTICLE_DESIGN {get; set;}

public:

property MDPropertyValue^ ARTICLE_DESIGN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property of a part variant. Type of plug construction according to specifications in the manufacturer catalog or according to DIN 41 612.
