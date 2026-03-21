# FUNC_ARTICLE_DESCR3 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_DESCR3(Int32).html

---

Part: Designation 3 # 20203.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_DESCR3( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_DESCR3 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Outputs the "Designation 3" property of the nth part using the index.
