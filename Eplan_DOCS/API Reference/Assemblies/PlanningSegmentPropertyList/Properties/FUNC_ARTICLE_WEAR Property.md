# FUNC_ARTICLE_WEAR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_WEAR(Int32).html

---

Wearing part # 20908.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_WEAR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_WEAR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Identifies a wearing part, e.g. the position of an item that is especially prone to wear. A max. of 50 definitions can be defined using the index.
