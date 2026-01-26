# ARTICLE_FREE_DATA_FULL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_FREE_DATA_FULL(Int32).html

---

Free properties: Value and unit (full) # 22234.

Syntax

**C#**



public PropertyValue ARTICLE_FREE_DATA_FULL( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_FREE_DATA_FULL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Value of a free property with specification of the unit. More than 1000 assignments can be made using the index. The full value with all decimal places is always stored; the value is not rounded up. This ensures precision is retained when converting to a different unit.
