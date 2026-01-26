# FUNC_ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic979.html

---

Subset / length # 31008.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PARTIAL_LENGTH( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PARTIAL_LENGTH {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Subset of a part, e.g. 5 pieces of a part, which are only provided in conduits of up to 100. At parts for cables, connections and their accessories (for example shrink tubes or insulating tubes) the contents of this property is evaluated as a length with specification of the displayed measuring unit and the entry of decimal values is possible, for example "0.7 m". If you do not enter a unit, the unit of length specified in the project settings is used. The value entered here is synchronized with the cable length (Length field in the Cable tab of the property dialog) for the main part of a cable. Using the index, you can differentiate between 50 entries.
