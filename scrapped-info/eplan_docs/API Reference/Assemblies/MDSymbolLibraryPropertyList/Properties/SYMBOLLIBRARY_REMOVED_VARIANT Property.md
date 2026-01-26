# SYMBOLLIBRARY_REMOVED_VARIANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBOLLIBRARY_REMOVED_VARIANT().html

---

Compressed symbol library # 15031.

Syntax

**C#**



public MDPropertyValue SYMBOLLIBRARY_REMOVED_VARIANT {get; set;}

public:

property MDPropertyValue^ SYMBOLLIBRARY_REMOVED_VARIANT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is assigned to a symbol library if one or more symbol variants were deleted from the symbol library during compression. In a comparison with the complete symbol library, however, the compressed symbol library is still considered equal in the system master data.
