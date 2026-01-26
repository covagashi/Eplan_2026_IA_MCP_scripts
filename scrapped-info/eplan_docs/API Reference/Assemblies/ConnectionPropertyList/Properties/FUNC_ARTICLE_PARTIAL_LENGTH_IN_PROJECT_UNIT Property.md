# FUNC_ARTICLE_PARTIAL_LENGTH_IN_PROJECT_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic166.html

---

Subset / length in unit of project # 31040.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PARTIAL_LENGTH_IN_PROJECT_UNIT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PARTIAL_LENGTH_IN_PROJECT_UNIT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Subset or length of the part converted into the unit which is specified in the project settings. The units are not displayed.
