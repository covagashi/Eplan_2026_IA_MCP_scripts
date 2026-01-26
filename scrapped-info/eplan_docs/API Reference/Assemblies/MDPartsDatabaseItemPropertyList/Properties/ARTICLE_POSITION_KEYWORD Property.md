# ARTICLE_POSITION_KEYWORD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_POSITION_KEYWORD().html

---

Performance description, standardized: Item keyword (device, utility, service) # 26536.

Syntax

**C#**



public MDPropertyValue ARTICLE_POSITION_KEYWORD {get; set;}

public:

property MDPropertyValue^ ARTICLE_POSITION_KEYWORD {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

The item keyword describes the type of service to be carried out, for example heating installation, sanitary installation or ventilation system.
