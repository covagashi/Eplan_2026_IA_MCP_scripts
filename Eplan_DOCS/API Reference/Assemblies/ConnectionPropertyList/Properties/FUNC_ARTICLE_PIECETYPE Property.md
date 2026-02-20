# FUNC_ARTICLE_PIECETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PIECETYPE(Int32).html

---

Part group # 20903.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PIECETYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PIECETYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Part groups are used to group parts of the same type, e.g., in heat or vibration sensitive items. A max. of 50 part groups can be defined using the index.

Changes done on this property are also visible on properties: \* ARTICLEREF\_PIECETYPE of corresponding [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).
