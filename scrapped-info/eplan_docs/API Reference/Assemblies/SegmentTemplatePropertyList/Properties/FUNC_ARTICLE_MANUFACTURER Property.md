# FUNC_ARTICLE_MANUFACTURER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_MANUFACTURER(Int32).html

---

Manufacturer # 20921.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MANUFACTURER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MANUFACTURER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

A max. of 50 manufacturers can be defined using the index.

Changes done on this property are also visible on properties: \* ARTICLE\_MANUFACTURER of corresponding [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).
