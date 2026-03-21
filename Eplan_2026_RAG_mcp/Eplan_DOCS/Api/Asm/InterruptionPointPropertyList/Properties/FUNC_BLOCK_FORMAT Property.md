# FUNC_BLOCK_FORMAT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList~FUNC_BLOCK_FORMAT(Int32).html

---

Block property: Format # 20202.

Syntax

**C#**



public PropertyValue FUNC_BLOCK_FORMAT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_BLOCK_FORMAT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

Selects which properties are specified in the relevant block property. Indirect properties cannot be output via block properties. The common index represents associated block and format properties.
