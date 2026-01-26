# SYMBLIB_PLACEDPROPERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_PLACEDPROPERROR(Int32).html

---

Error: Property placement # 15106.

Syntax

**C#**



public MDPropertyValue SYMBLIB_PLACEDPROPERROR( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMBLIB_PLACEDPROPERROR {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Indicates whether a problem occurred with any placed properties during the data transfer of symbol libraries. Max. of 1,024 are recorded.
