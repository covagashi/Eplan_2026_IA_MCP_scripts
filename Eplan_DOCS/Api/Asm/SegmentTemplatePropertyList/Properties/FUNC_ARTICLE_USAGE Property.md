# FUNC_ARTICLE_USAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_USAGE(Int32).html

---

Procurement # 20911.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_USAGE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_USAGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Estimated time required to obtain the part. A max. of 50 definitions can be defined using the index.
