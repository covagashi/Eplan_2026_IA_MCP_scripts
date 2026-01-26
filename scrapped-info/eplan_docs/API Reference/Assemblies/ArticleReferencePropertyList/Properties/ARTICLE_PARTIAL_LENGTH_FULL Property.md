# ARTICLE_PARTIAL_LENGTH_FULL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_PARTIAL_LENGTH_FULL().html

---

Subset / length (full) # 20510.

Syntax

**C#**



public PropertyValue ARTICLE_PARTIAL_LENGTH_FULL {get; set;}

public:

property PropertyValue^ ARTICLE_PARTIAL_LENGTH_FULL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Subset of a part with information about the unit. At parts for cables, connections and their accessories (for example shrink tubes or insulating tubes) the contents of this property is evaluated as a length and the entry of decimal values is possible, for example "0.7 m". The full value with all decimal places is always stored; the value is not rounded up. This ensures precision is retained when converting to a different unit. This property may be used in bills of materials, for example.
