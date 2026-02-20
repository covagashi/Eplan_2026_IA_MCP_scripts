# FUNC_ARTICLE_FLOW_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_FLOW_DIRECTION(Int32).html

---

Flow direction: Operating flow direction # 26268.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FLOW_DIRECTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FLOW_DIRECTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Direction of flow of a hydraulic device during the normal operation of a system. This specification is relevant for the correct function and efficiency of measuring instruments and control valves, which possibly must only work in a specific direction.
