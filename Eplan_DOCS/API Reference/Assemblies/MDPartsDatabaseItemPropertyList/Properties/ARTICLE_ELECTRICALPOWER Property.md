# ARTICLE_ELECTRICALPOWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_ELECTRICALPOWER().html

---

Switching capacity # 22072.

Syntax

**C#**



public MDPropertyValue ARTICLE_ELECTRICALPOWER {get; set;}

public:

property MDPropertyValue^ ARTICLE_ELECTRICALPOWER {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Electrical switching capacity (in watt) of a contact at coils of contactors and relays or of a component. At a part with the product group "Relays, contactors" this property refers to the contact.
