# FUNC_ARTICLE_VARIANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_VARIANT(Int32).html

---

Part variant # 20101.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_VARIANT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_VARIANT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Shows a max. of 50 variants of the part number assigned to a function.
