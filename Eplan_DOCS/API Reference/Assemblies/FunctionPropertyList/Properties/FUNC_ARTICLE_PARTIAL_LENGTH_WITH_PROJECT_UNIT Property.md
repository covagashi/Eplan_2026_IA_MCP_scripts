# FUNC_ARTICLE_PARTIAL_LENGTH_WITH_PROJECT_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic230.html

---

Subset / length with unit of project # 31043.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PARTIAL_LENGTH_WITH_PROJECT_UNIT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PARTIAL_LENGTH_WITH_PROJECT_UNIT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Subset or length of the part including unit converted into the unit which is specified in the project settings. Using the index, you can differentiate between 50 entries.
