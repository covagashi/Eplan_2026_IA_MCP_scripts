# FUNC_ARTICLE_PARTIAL_LENGTH_VALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_PARTIAL_LENGTH_VALUE(Int32).html

---

Subset / length: Value # 31010.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PARTIAL_LENGTH_VALUE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PARTIAL_LENGTH_VALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Value of the subset of the part without information about the unit. At parts for cables, connections and their accessories (for example shrink tubes or insulating tubes) the contents of this property is evaluated as a length in "meter" and the entry of decimal values is possible. Using the index, you can differentiate between 50 entries.
