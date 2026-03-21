# ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION(Int32).html

---

External document: Designation # 22279.

Syntax

**C#**



public PropertyValue ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 20.
