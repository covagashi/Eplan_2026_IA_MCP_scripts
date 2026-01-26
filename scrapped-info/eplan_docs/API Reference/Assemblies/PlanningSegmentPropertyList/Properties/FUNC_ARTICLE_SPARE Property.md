# FUNC_ARTICLE_SPARE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_SPARE(Int32).html

---

Spare part # 20907.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SPARE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SPARE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Identifies a spare part, e.g. the name of the item that can replace the defective or worn part. A max. of 50 definitions can be defined using the index.
