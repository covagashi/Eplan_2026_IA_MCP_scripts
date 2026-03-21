# FUNC_ARTICLE_PUMPING_VOLUME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1012.html

---

Quantity / subset in unit of project # 31044.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_QUANTITY_IN_PROJECT_UNIT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_QUANTITY_IN_PROJECT_UNIT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Quantity or subset of a part converted into the unit which is specified in the project settings. The units are not displayed. If the property "Subset / length" has a value (not 0), then this value is entered for "Quantity / subset" in reports, otherwise "Quantity" is used. Using the index, you can differentiate between 50 entries.
