# FUNC_ARTICLE_REPLACEMENT_FOR_PRODUCT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_REPLACEMENT_FOR_PRODUCT(Int32).html

---

Replacement part: Original part # 26319.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_REPLACEMENT_FOR_PRODUCT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_REPLACEMENT_FOR_PRODUCT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Type designation of the original part for which this part is offered as a replacement.
