# SYMBLIB_ERRORSYMBOLED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_ERRORSYMBOLED(Int32).html

---

Error (symbol editor) # 15201.

Syntax

**C#**



public MDPropertyValue SYMBLIB_ERRORSYMBOLED( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMBLIB_ERRORSYMBOLED {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Shows whether a problem occurred during the symbol libraries data transfer that can be solved in the symbol editor. Max. of 1,024 are recorded.
