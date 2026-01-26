# SYMB_CABLE_RELATED_VDP_SYMBOL_ID_USE_1ST_VARIANT_ONLY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1727.html

---

Use first variant of connection definition point symbol # 16030.

Syntax

**C#**



public MDPropertyValue SYMB_CABLE_RELATED_VDP_SYMBOL_ID_USE_1ST_VARIANT_ONLY {get; set;}

public:

property MDPropertyValue^ SYMB_CABLE_RELATED_VDP_SYMBOL_ID_USE_1ST_VARIANT_ONLY {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

The corresponding variants are normally always used when placing cable symbols and their relevant connection definition point symbols. If this property is enabled, the first variant of the connection definition point symbol is always used when placing or moving the cable symbol.
