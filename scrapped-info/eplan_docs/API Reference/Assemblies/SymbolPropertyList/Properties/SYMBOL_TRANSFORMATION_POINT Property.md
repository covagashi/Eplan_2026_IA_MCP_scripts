# SYMBOL_TRANSFORMATION_POINT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMBOL_TRANSFORMATION_POINT(Int32).html

---

Transformation point # 16045.

Syntax

**C#**



public PropertyValue SYMBOL_TRANSFORMATION_POINT( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMBOL_TRANSFORMATION_POINT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 16.

The transformation point is used as the base point for rotation and flipping. Each symbol variant can have its own transformation point; symbol variants are distinguished via the index. The transformation point is entered as a coordinate in mm, e.g., "2.0/2.0". The entry refers to the insertion point of the respective symbol variant. If a transformation point has not been defined for a symbol variant, the first connection point of the symbol will be used as a base point.
