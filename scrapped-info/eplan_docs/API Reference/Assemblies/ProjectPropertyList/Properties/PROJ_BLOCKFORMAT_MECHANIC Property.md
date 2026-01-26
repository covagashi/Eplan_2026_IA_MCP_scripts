# PROJ_BLOCKFORMAT_MECHANIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_MECHANIC(Int32).html

---

Block property: Format (mechanical) # 10619.

Syntax

**C#**



public PropertyValue PROJ_BLOCKFORMAT_MECHANIC( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_BLOCKFORMAT_MECHANIC {

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
