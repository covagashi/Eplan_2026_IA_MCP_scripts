# FUNC_ARTICLE_TYPE_OF_USE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TYPE_OF_USE(Int32).html

---

Operating mode # 26284.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TYPE_OF_USE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TYPE_OF_USE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The way in which a product or service is used.
