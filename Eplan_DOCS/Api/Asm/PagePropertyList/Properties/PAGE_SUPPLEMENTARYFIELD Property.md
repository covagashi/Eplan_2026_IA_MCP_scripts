# PAGE_SUPPLEMENTARYFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_SUPPLEMENTARYFIELD(Int32).html

---

Supplementary field # 11901.

Syntax

**C#**



public PropertyValue PAGE_SUPPLEMENTARYFIELD( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_SUPPLEMENTARYFIELD {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Max. 1,000 words in the supplementary fields for the page that can be specified using the index.
