# ARTICLE_HOLDINGPOWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_HOLDINGPOWER().html

---

Holding power # 22073.

Syntax

**C#**



public MDPropertyValue ARTICLE_HOLDINGPOWER {get; set;}

public:

property MDPropertyValue^ ARTICLE_HOLDINGPOWER {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Maximum holding power (in mVA) of contactor and relay coils. At a part with the product group "Relays, contactors" this property refers to the coil.
