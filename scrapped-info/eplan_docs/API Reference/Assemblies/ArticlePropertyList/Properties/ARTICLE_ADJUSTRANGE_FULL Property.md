# ARTICLE_ADJUSTRANGE_FULL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADJUSTRANGE_FULL().html

---

Control range (full) # 22231.

Syntax

**C#**



public PropertyValue ARTICLE_ADJUSTRANGE_FULL {get; set;}

public:

property PropertyValue^ ARTICLE_ADJUSTRANGE_FULL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Control range with information about the unit. The full value with all decimal places is always stored; the value is not rounded up. This ensures precision is retained when converting to a different unit.
