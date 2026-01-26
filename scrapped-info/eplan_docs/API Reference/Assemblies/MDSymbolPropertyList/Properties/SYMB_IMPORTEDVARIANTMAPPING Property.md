# SYMB_IMPORTEDVARIANTMAPPING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_IMPORTEDVARIANTMAPPING(Int32).html

---

Symbol variant assignment (internal) # 16031.

Syntax

**C#**



public MDPropertyValue SYMB_IMPORTEDVARIANTMAPPING( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMB_IMPORTEDVARIANTMAPPING {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 4.

This property is populated during the data transfer of projects from EPLAN 5. It is only required for EPLAN 5 due to compatibility reasons and is no longer used in new projects. The assignment of the variants for data transfer is stored here.
