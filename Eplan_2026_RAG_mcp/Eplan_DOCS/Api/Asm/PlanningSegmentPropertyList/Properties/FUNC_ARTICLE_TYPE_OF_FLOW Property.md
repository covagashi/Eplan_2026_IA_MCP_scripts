# FUNC_ARTICLE_TYPE_OF_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_TYPE_OF_FLOW(Int32).html

---

Type of flow # 26220.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TYPE_OF_FLOW( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TYPE_OF_FLOW {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The way in which a medium (e.g., liquid or gas) flows through a system or component. The value can be specified as mass flow or volume flow.
