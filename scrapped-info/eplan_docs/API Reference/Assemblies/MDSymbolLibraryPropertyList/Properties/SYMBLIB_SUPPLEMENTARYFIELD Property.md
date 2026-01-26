# SYMBLIB_SUPPLEMENTARYFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_SUPPLEMENTARYFIELD(Int32).html

---

Supplementary field # 15901.

Syntax

**C#**



public MDPropertyValue SYMBLIB_SUPPLEMENTARYFIELD( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMBLIB_SUPPLEMENTARYFIELD {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Max. 1,000 supplementary fields for the symbol library that can be specified using the index.
