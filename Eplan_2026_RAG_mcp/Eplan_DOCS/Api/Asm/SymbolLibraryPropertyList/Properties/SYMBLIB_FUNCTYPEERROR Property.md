# SYMBLIB_FUNCTYPEERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_FUNCTYPEERROR(Int32).html

---

Error: Representation type # 15103.

Syntax

**C#**



public PropertyValue SYMBLIB_FUNCTYPEERROR( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMBLIB_FUNCTYPEERROR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Indicates whether a problem occurred with any representation type during the data transfer of symbol libraries. Max. of 1,024 are recorded.
