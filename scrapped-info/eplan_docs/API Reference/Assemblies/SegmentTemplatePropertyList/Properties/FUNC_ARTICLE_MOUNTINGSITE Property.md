# FUNC_ARTICLE_MOUNTINGSITE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_MOUNTINGSITE(Int32).html

---

Part: Mounting surface # 20918.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MOUNTINGSITE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MOUNTINGSITE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

A max. of 50 mounting surfaces can be defined using the index.
