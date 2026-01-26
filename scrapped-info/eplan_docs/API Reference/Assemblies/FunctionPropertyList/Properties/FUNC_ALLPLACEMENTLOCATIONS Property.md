# FUNC_ALLPLACEMENTLOCATIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ALLPLACEMENTLOCATIONS(Int32).html

---

All placements # 20477.

Syntax

**C#**



public PropertyValue FUNC_ALLPLACEMENTLOCATIONS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ALLPLACEMENTLOCATIONS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Outputs the placements of any representation type of the function.
