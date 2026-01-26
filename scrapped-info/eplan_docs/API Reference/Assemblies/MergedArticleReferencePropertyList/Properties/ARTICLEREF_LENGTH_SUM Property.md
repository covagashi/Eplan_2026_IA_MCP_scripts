# ARTICLEREF_LENGTH_SUM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_LENGTH_SUM().html

---

Total length with unit of the project # 20513.

Syntax

**C#**



public PropertyValue ARTICLEREF_LENGTH_SUM {get; set;}

public:

property PropertyValue^ ARTICLEREF_LENGTH_SUM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property totals up the lengths of all the functions (for example, cables, connections, routing paths, busbars, etc.) having the same part. The unit of length is specified in the project settings for cables. Only at connections does the unit come from the project settings for connections. You can use the property in forms for the summarized parts list, for example in calculation formulas for calculating the order length.
