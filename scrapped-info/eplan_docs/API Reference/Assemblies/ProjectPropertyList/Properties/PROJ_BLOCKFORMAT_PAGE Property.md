# PROJ_BLOCKFORMAT_PAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_PAGE(Int32).html

---

Block property: Format (page) # 10618.

Syntax

**C#**



public PropertyValue PROJ_BLOCKFORMAT_PAGE( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_BLOCKFORMAT_PAGE {

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
