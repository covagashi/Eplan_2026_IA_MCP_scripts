# SYMBLIB_IMPORTERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_IMPORTERROR(Int32).html

---

Error (import) # 15200.

Syntax

**C#**



public PropertyValue SYMBLIB_IMPORTERROR( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMBLIB_IMPORTERROR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Shows whether a problem occurred during the symbol libraries data transfer that can be solved in the function definition assignment dialog. Max. of 1,024 are recorded.
