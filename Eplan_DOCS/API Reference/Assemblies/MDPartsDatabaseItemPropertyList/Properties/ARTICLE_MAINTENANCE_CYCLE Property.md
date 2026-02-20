# ARTICLE_MAINTENANCE_CYCLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MAINTENANCE_CYCLE().html

---

Maintenance cycle # 26637.

Syntax

**C#**



public MDPropertyValue ARTICLE_MAINTENANCE_CYCLE {get; set;}

public:

property MDPropertyValue^ ARTICLE_MAINTENANCE_CYCLE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Describes the entire sequence of maintenance activities that must be performed within a specific time period or after a specific number of hours of operation. A maintenance cycle can include multiple maintenance intervals and ensures that all necessary maintenance work is performed over time.
