# ARTICLE_PRODUCT_FUNCTION_WITH_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRODUCT_FUNCTION_WITH_BACNET().html

---

BACnet: Product function # 26538.

Syntax

**C#**



public PropertyValue ARTICLE_PRODUCT_FUNCTION_WITH_BACNET {get; set;}

public:

property PropertyValue^ ARTICLE_PRODUCT_FUNCTION_WITH_BACNET {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

The product function describes the specific tasks and capabilities of a product within a BACnet network, e.g. temperature control, light control, etc.
