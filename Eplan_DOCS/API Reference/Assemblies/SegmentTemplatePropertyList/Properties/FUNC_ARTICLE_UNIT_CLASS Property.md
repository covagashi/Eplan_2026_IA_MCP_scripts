# FUNC_ARTICLE_UNIT_CLASS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_UNIT_CLASS(Int32).html

---

Device class # 26367.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_UNIT_CLASS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_UNIT_CLASS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Degree of protection of a housing. Specifies how well a device is protected against electric shocks.
