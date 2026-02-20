# SYMBLIB_CONNECTIONERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_CONNECTIONERROR(Int32).html

---

Error: Connection point # 15101.

Syntax

**C#**



public MDPropertyValue SYMBLIB_CONNECTIONERROR( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMBLIB_CONNECTIONERROR {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Indicates whether a problem occurred with any connection points during the data transfer of symbol libraries. Max. of 1,024 are recorded.
