# FUNC_ARTICLE_WEIGHT_KG_1000_M Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_WEIGHT_KG_1000_M(Int32).html

---

Weight (in kg/1000 m) # 26375.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_WEIGHT_KG_1000_M( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_WEIGHT_KG_1000_M {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Weight of a part per 1000 meters of length. This specification is relevant for length-related parts such as cables, wires, pipes, etc.
