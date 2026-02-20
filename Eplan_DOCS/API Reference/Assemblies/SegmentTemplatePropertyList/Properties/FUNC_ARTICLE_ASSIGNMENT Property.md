# FUNC_ARTICLE_ASSIGNMENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_ASSIGNMENT(Int32).html

---

Part allocation # 20904.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ASSIGNMENT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ASSIGNMENT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Defines whether the assigned part is the main part or an accessory part. A max. of 50 part assignments can be defined using the index.
