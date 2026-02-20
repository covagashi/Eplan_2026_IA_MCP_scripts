# FUNC_ARTICLE_LENGTH_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_LENGTH_MAX(Int32).html

---

Length, max. # 26414.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_LENGTH_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_LENGTH_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum length of a product or a component.
