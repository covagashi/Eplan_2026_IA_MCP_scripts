# ARTICLE_POWERDISSIPATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_POWERDISSIPATION().html

---

Max. power dissipation # 22074.

Syntax

**C#**



public MDPropertyValue ARTICLE_POWERDISSIPATION {get; set;}

public:

property MDPropertyValue^ ARTICLE_POWERDISSIPATION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Specification of the maximum power dissipation (in watt) at coils of contactors and relays. At a part with the product group "Relays, contactors" this property refers to the coil.
