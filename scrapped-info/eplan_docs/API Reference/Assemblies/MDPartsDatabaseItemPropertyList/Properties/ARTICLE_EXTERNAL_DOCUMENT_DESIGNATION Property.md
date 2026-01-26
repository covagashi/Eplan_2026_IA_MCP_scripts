# ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1559.html

---

External document: Designation # 22279.

Syntax

**C#**



public MDPropertyValue ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 20.
