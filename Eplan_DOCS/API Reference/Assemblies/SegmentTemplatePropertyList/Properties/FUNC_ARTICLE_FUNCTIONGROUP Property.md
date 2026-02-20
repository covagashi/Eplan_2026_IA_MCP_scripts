# FUNC_ARTICLE_FUNCTIONGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_FUNCTIONGROUP(Int32).html

---

Function group # 20902.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FUNCTIONGROUP( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FUNCTIONGROUP {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

This field is for informational purposes and can be used, for instance, for filtering during part selection. A max. of 50 function groups can be defined using the index.
