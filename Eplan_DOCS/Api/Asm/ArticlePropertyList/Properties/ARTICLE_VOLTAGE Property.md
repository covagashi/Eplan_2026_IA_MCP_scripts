# ARTICLE_VOLTAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLTAGE().html

---

Voltage # 22033.

Syntax

**C#**



public PropertyValue ARTICLE_VOLTAGE {get; set;}

public:

property PropertyValue^ ARTICLE_VOLTAGE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Coil operating voltage or of the component (connection point voltage for electricity consumers). At a part with the product group "Relays, contactors" this property refers to the coil.
