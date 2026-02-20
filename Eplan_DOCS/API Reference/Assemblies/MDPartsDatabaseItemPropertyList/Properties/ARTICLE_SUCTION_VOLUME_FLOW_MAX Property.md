# ARTICLE_SUCTION_VOLUME_FLOW_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_SUCTION_VOLUME_FLOW_MAX().html

---

Intake flow rate, max. # 26198.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUCTION_VOLUME_FLOW_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUCTION_VOLUME_FLOW_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum flow rate within the working range of the conveyed gas at the outlet point of a fluid machine in relation to the conditions prevailing at the inlet point for the total temperature, the total pressure and the gas composition (e.g. humidity).
