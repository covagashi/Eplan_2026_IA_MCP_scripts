# ARTICLE_POWERDISSIPATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWERDISSIPATION().html

---

Max. power dissipation # 22074.

Syntax

**C#**



public PropertyValue ARTICLE_POWERDISSIPATION {get; set;}

public:

property PropertyValue^ ARTICLE_POWERDISSIPATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Specification of the maximum power dissipation (in watt) at coils of contactors and relays. At a part with the product group "Relays, contactors" this property refers to the coil.
