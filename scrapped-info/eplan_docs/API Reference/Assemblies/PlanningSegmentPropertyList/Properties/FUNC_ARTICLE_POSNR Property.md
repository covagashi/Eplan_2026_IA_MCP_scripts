# FUNC_ARTICLE_POSNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_POSNR(Int32).html

---

Item number # 20464.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_POSNR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POSNR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Shows the position number of a part in indexed form. The value can be either manually or automatically entered in the bill of materials navigator.
