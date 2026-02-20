# ARTICLE_FREE_DATA_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREE_DATA_DESCRIPTION(Int32).html

---

Free properties: Displayed name # 22146.

Syntax

**C#**



public PropertyValue ARTICLE_FREE_DATA_DESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_FREE_DATA_DESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Description of the free property. More than 1000 assignments can be made using the index.
