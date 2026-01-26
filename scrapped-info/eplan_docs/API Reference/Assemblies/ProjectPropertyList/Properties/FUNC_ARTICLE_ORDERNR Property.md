# FUNC_ARTICLE_ORDERNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ORDERNR(Int32).html

---

Order number # 20919.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ORDERNR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ORDERNR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

A max. of 50 order numbers can be defined using the index.
