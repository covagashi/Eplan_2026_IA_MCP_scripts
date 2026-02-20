# ARTICLE_IDENTCODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_IDENTCODE().html

---

Barcode number # 22208.

Syntax

**C#**



public MDPropertyValue ARTICLE_IDENTCODE {get; set;}

public:

property MDPropertyValue^ ARTICLE_IDENTCODE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Barcodes are used to give goods a unique identification. Different coding standards are used internationally, for example the GTIN (Global Trade Item Number). In addition, companies use company-specific or industrial standards.

The contents of this property can be taken into account in manufacturing lists and when importing and exporting parts. However, it cannot be translated.
