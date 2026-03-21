# ARTICLE_GROUPSYMBOLMACRO_CUSTOM_MACRO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic54.html

---

Schematic macro: Macro for company standard # 22881.

Syntax

**C#**



public PropertyValue ARTICLE_GROUPSYMBOLMACRO_CUSTOM_MACRO( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_GROUPSYMBOLMACRO_CUSTOM_MACRO {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

2D macro that can be placed on schematic pages as well as 2D panel layout pages. Together with the Schematic macro: Name for company standard property, macros are defined that are to be used in projects for a specific company standard.
