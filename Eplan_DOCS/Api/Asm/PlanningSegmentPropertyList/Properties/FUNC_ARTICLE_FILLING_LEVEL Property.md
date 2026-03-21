# FUNC_ARTICLE_FILLING_LEVEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_FILLING_LEVEL(Int32).html

---

Fill capacity # 26345.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FILLING_LEVEL( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FILLING_LEVEL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Ratio of the volume actually used to the maximum available volume of a container or space.
