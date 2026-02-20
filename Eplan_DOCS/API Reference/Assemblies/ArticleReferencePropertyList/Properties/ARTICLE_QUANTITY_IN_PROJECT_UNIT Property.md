# ARTICLE_QUANTITY_IN_PROJECT_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_QUANTITY_IN_PROJECT_UNIT().html

---

Quantity / subset in unit of project # 20507.

Syntax

**C#**



public PropertyValue ARTICLE_QUANTITY_IN_PROJECT_UNIT {get; set;}

public:

property PropertyValue^ ARTICLE_QUANTITY_IN_PROJECT_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Quantity or subset of a part converted into the unit which is specified in the project settings. The units are not displayed. If the property "Subset / length" has a value (not 0), then this value is entered for "Quantity / subset" in reports, otherwise "Quantity" is used.
