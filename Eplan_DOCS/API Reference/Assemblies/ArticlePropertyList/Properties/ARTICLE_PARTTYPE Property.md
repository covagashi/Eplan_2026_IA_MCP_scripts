# ARTICLE_PARTTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PARTTYPE().html

---

Record type # 22023.

Syntax

**C#**



public PropertyValue ARTICLE_PARTTYPE {get; set;}

public:

property PropertyValue^ ARTICLE_PARTTYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property shows the type of parts data or cross-part data, such as component, assembly, accessory list, drilling pattern, customer. For parts data and for addresses you can change the record type via the drop-down list (for parts data: component, assembly, module, supplemental part; for addresses: customer, manufacturer / supplier).
