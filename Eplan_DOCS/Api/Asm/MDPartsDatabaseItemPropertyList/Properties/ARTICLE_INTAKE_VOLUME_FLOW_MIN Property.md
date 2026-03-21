# ARTICLE_INTAKE_VOLUME_FLOW_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_INTAKE_VOLUME_FLOW_MIN().html

---

Intake flow rate, min. # 26200.

Syntax

**C#**



public MDPropertyValue ARTICLE_INTAKE_VOLUME_FLOW_MIN {get; set;}

public:

property MDPropertyValue^ ARTICLE_INTAKE_VOLUME_FLOW_MIN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum flow rate within the working range of the conveyed gas at the outlet point of a fluid machine in relation to the conditions prevailing at the inlet point for the total temperature, the total pressure and the gas composition (e.g. humidity).
