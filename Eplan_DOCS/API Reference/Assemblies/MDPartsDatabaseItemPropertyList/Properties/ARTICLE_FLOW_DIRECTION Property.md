# ARTICLE_FLOW_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FLOW_DIRECTION().html

---

Flow direction: Operating flow direction # 26267.

Syntax

**C#**



public MDPropertyValue ARTICLE_FLOW_DIRECTION {get; set;}

public:

property MDPropertyValue^ ARTICLE_FLOW_DIRECTION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Direction of flow of a hydraulic device during the normal operation of a system. This specification is relevant for the correct function and efficiency of measuring instruments and control valves, which possibly must only work in a specific direction.
