# FUNC_ARTICLE_STRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_STRESS(Int32).html

---

Stress # 20910.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_STRESS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_STRESS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The types of stress differentiate between mechanical movement values (static and dynamic) and environmental influences (e.g., moisture, heat, chemical reactions). A max. of 50 definitions can be defined using the index.
