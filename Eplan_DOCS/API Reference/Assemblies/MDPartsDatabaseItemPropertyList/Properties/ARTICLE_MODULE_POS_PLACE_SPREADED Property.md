# ARTICLE_MODULE_POS_PLACE_SPREADED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MODULE_POS_PLACE_SPREADED().html

---

Distributed placement of module # 22288.

Syntax

**C#**



public MDPropertyValue ARTICLE_MODULE_POS_PLACE_SPREADED {get; set;}

public:

property MDPropertyValue^ ARTICLE_MODULE_POS_PLACE_SPREADED {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Property of a part variant. Controls how a module is placed in Eplan Pro Panel:

0 = Place module parts and elements

1 = Place only module parts

2 = Place only elements
