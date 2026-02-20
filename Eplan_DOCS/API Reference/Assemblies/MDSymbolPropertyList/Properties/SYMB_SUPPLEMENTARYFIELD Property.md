# SYMB_SUPPLEMENTARYFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_SUPPLEMENTARYFIELD(Int32).html

---

Supplementary field # 16013.

Syntax

**C#**



public MDPropertyValue SYMB_SUPPLEMENTARYFIELD( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMB_SUPPLEMENTARYFIELD {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 99.

Max. 99 supplementary fields for the symbol that can be specified using the index.
