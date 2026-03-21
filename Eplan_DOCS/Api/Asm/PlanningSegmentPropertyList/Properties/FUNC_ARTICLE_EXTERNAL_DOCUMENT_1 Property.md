# FUNC_ARTICLE_EXTERNAL_DOCUMENT_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic911.html

---

Part: External document 10 # 20269.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_EXTERNAL_DOCUMENT_10( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EXTERNAL_DOCUMENT_10 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Outputs the "External document 10" property of the nth part using the index.
