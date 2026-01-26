# FUNC_ARTICLE_EXTERNAL_DOCUMENT_12 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic914.html

---

Part: External document 13 # 20272.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_EXTERNAL_DOCUMENT_13( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EXTERNAL_DOCUMENT_13 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Outputs the "External document 13" property of the nth part using the index.
