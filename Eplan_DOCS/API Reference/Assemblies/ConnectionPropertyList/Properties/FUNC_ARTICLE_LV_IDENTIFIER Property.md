# FUNC_ARTICLE_LV_IDENTIFIER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LV_IDENTIFIER(Int32).html

---

Bill of quantities: Identifier # 26439.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_LV_IDENTIFIER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_LV_IDENTIFIER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

This identifier is used to uniquely identify and classify a bill of quantities.
