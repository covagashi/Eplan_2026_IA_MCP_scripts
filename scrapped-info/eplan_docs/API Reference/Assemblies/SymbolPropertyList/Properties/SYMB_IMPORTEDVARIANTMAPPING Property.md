# SYMB_IMPORTEDVARIANTMAPPING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_IMPORTEDVARIANTMAPPING(Int32).html

---

Symbol variant assignment (internal) # 16031.

Syntax

**C#**



public PropertyValue SYMB_IMPORTEDVARIANTMAPPING( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMB_IMPORTEDVARIANTMAPPING {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 4.

This property is populated during the data transfer of projects from EPLAN 5. It is only required for EPLAN 5 due to compatibility reasons and is no longer used in new projects. The assignment of the variants for data transfer is stored here.
