# FUNC_ARTICLE_WEIGHT_OF_THE_PACKAGING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_WEIGHT_OF_THE_PACKAGING(Int32).html

---

Weight (packaging) # 26379.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_WEIGHT_OF_THE_PACKAGING( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_WEIGHT_OF_THE_PACKAGING {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Total weight of the packaging of a product. This can include both the primary packaging (directly around the product) as well as the secondary packaging (additional protective packaging).
