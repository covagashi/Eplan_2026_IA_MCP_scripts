# SYMBLIB_FUNCDEFERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_FUNCDEFERROR(Int32).html

---

Error: Function definition # 15100.

Syntax

**C#**



public MDPropertyValue SYMBLIB_FUNCDEFERROR( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMBLIB_FUNCDEFERROR {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Indicates whether a function definition was missing during the data transfer of symbol libraries. Max. of 1,024 are recorded.
