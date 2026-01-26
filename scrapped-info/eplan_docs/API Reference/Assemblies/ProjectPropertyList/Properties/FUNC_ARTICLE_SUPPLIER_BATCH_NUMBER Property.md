# FUNC_ARTICLE_SUPPLIER_BATCH_NUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_SUPPLIER_BATCH_NUMBER(Int32).html

---

Supplier batch number # 26436.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SUPPLIER_BATCH_NUMBER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SUPPLIER_BATCH_NUMBER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

One-time and unique alphanumeric identifier used to uniquely identify products from different manufacturing processes.
