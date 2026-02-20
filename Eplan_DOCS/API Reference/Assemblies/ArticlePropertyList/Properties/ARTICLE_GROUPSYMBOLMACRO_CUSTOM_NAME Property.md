# ARTICLE_GROUPSYMBOLMACRO_CUSTOM_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_CUSTOM_NAME(Int32).html

---

Schematic macro: Name for company standard # 22880.

Syntax

**C#**



public PropertyValue ARTICLE_GROUPSYMBOLMACRO_CUSTOM_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_GROUPSYMBOLMACRO_CUSTOM_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

Name of the company standard for schematic macros. Together with the Schematic macro: Macro for company standard property, macros are defined that are to be used in projects for a specific company standard.
