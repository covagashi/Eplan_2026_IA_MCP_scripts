# FUNC_ARTICLE_WEIGHT_TOTAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_WEIGHT_TOTAL(Int32).html

---

Total weight (part) # 26373.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_WEIGHT_TOTAL( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_WEIGHT_TOTAL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Total weight of the part including all relevant components such as housing or supplemental parts.
