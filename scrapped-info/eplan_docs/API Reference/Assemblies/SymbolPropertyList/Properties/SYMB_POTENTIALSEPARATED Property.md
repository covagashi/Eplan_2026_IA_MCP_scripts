# SYMB_POTENTIALSEPARATED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_POTENTIALSEPARATED().html

---

With signal isolation # 16042.

Syntax

**C#**



public PropertyValue SYMB_POTENTIALSEPARATED {get; set;}

public:

property PropertyValue^ SYMB_POTENTIALSEPARATED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows whether a function with signal isolation is generated when using the symbol. The visibility of the property depends on the type of symbol. The following values are possible:

0 = Not defined (The property is not observed when placing and replacing the symbol.)

1 = Yes (A function with signal isolation is generated for this symbol when placing and replacing the symbol.)

2 = No (A function without signal isolation is generated for this symbol when placing and replacing the symbol.)
