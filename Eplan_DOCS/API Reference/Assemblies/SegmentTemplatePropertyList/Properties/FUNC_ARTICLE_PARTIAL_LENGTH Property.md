# FUNC_ARTICLE_PARTIAL_LENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1206.html

---

Subset / length (full) # 31091.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PARTIAL_LENGTH_FULL( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PARTIAL_LENGTH_FULL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Subset of a part, entered for the function, with information about the unit. At parts for cables, connections and their accessories (for example shrink tubes or insulating tubes) the contents of this property is evaluated as a length and the entry of decimal values is possible, for example "0.7 m". The full value with all decimal places is always stored; the value is not rounded up. This ensures precision is retained when converting to a different unit. Using the index, you can differentiate between 50 entries.
