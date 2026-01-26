# ARTICLE_PARTIAL_LENGTH_VALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_PARTIAL_LENGTH_VALUE().html

---

Subset / length: Value # 20497.

Syntax

**C#**



public PropertyValue ARTICLE_PARTIAL_LENGTH_VALUE {get; set;}

public:

property PropertyValue^ ARTICLE_PARTIAL_LENGTH_VALUE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Value of the subset of the part without information about the unit. At parts for cables, connections and their accessories (for example shrink tubes or insulating tubes) the contents of this property is evaluated as a length in "meter" and the entry of decimal values is possible.
