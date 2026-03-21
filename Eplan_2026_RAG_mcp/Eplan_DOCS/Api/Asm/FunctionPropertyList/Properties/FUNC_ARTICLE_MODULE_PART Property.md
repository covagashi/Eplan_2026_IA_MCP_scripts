# FUNC_ARTICLE_MODULE_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_MODULE_PART(Int32).html

---

Part is included in a module # 20906.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MODULE_PART( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MODULE_PART {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specifies whether this part is part of a module. A max. of 50 definitions can be defined using the index.
