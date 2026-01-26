# ARTICLE_ELECTRICALPOWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ELECTRICALPOWER().html

---

Switching capacity # 22072.

Syntax

**C#**



public PropertyValue ARTICLE_ELECTRICALPOWER {get; set;}

public:

property PropertyValue^ ARTICLE_ELECTRICALPOWER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Electrical switching capacity (in watt) of a contact at coils of contactors and relays or of a component. At a part with the product group "Relays, contactors" this property refers to the contact.
