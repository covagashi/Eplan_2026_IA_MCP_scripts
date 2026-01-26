# FUNC_ARTICLE_EXTERNAL_DOCUMENT_11 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic913.html

---

Part: External document 12 # 20271.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_EXTERNAL_DOCUMENT_12( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EXTERNAL_DOCUMENT_12 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Outputs the "External document 12" property of the nth part using the index.
