# ARTICLE_HOLDINGPOWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HOLDINGPOWER().html

---

Holding power # 22073.

Syntax

**C#**



public PropertyValue ARTICLE_HOLDINGPOWER {get; set;}

public:

property PropertyValue^ ARTICLE_HOLDINGPOWER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Maximum holding power (in mVA) of contactor and relay coils. At a part with the product group "Relays, contactors" this property refers to the coil.
