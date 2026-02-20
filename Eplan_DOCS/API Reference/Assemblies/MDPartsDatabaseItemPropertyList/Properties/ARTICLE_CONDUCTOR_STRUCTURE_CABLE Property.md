# ARTICLE_CONDUCTOR_STRUCTURE_CABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONDUCTOR_STRUCTURE_CABLE().html

---

Conductor design (cable) # 26049.

Syntax

**C#**



public MDPropertyValue ARTICLE_CONDUCTOR_STRUCTURE_CABLE {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONDUCTOR_STRUCTURE_CABLE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specific structure and composition of electrical conductors within a cable. This includes details such as the number of conductors, the cross-section of the conductors, the material (e.g. copper or aluminum) and the type of insulation.
