# ARTICLE_MAINTENANCE_INTERVAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MAINTENANCE_INTERVAL().html

---

Maintenance interval # 26635.

Syntax

**C#**



public MDPropertyValue ARTICLE_MAINTENANCE_INTERVAL {get; set;}

public:

property MDPropertyValue^ ARTICLE_MAINTENANCE_INTERVAL {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specifies the period or operating hours between two maintenance tasks. Specification of how often a maintenance has to be carried out, for example every 6 months or every 500 operating hours.
