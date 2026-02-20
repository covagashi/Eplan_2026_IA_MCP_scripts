# SYMBLIB_GRAPHICERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_GRAPHICERROR(Int32).html

---

Error: Symbol graphic # 15105.

Syntax

**C#**



public MDPropertyValue SYMBLIB_GRAPHICERROR( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMBLIB_GRAPHICERROR {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Indicates whether a problem occurred with any symbol graphics during the data transfer of symbol libraries. Max. of 1,024 are recorded.
