# FUNC_BLOCK_VALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_BLOCK_VALUE(Int32).html

---

Block property # 20201.

Syntax

**C#**



public PropertyValue FUNC_BLOCK_VALUE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_BLOCK_VALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Shows the properties that have been specified in the relevant format property "Block property: Format [n]". The joint index [n] represents the relevant block and format properties.
