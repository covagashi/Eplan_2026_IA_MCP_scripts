# SYMBLIB_GRAPHICERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_GRAPHICERROR(Int32).html

---

Error: Symbol graphic # 15105.

Syntax

**C#**



public PropertyValue SYMBLIB_GRAPHICERROR( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMBLIB_GRAPHICERROR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Indicates whether a problem occurred with any symbol graphics during the data transfer of symbol libraries. Max. of 1,024 are recorded.
