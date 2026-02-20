# FUNC_ARTICLE_SUPPLIER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_SUPPLIER(Int32).html

---

Supplier # 20920.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SUPPLIER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SUPPLIER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

A max. of 50 suppliers can be defined using the index.
