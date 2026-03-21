# ARTICLE_PARTTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PARTTYPE().html

---

Record type # 22023.

Syntax

**C#**



public MDPropertyValue ARTICLE_PARTTYPE {get; set;}

public:

property MDPropertyValue^ ARTICLE_PARTTYPE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property shows the type of parts data or cross-part data, such as component, assembly, accessory list, drilling pattern, customer. For parts data and for addresses you can change the record type via the drop-down list (for parts data: component, assembly, module, supplemental part; for addresses: customer, manufacturer / supplier).
