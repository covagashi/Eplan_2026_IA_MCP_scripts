# SYMB_SUPPLEMENTARYFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_SUPPLEMENTARYFIELD(Int32).html

---

Supplementary field # 16013.

Syntax

**C#**



public PropertyValue SYMB_SUPPLEMENTARYFIELD( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMB_SUPPLEMENTARYFIELD {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 99.

Max. 99 supplementary fields for the symbol that can be specified using the index.
