# ARTICLE_FREE_DATA_NEWVALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_FREE_DATA_NEWVALUE(Int32).html

---

User-defined properties: Value # 22337.

Syntax

**C#**



public PropertyValue ARTICLE_FREE_DATA_NEWVALUE( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_FREE_DATA_NEWVALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.
