# FUNC_ARTICLE_LOCATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_LOCATION(Int32).html

---

Operating location # 26292.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_LOCATION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_LOCATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Physical locations or environments for which a product or component is suitable. Example: Outdoor area, indoor area.
