# SYMB_POTENTIALSEPARATED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_POTENTIALSEPARATED().html

---

With signal isolation # 16042.

Syntax

**C#**



public MDPropertyValue SYMB_POTENTIALSEPARATED {get; set;}

public:

property MDPropertyValue^ SYMB_POTENTIALSEPARATED {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows whether a function with signal isolation is generated when using the symbol. The visibility of the property depends on the type of symbol. The following values are possible:

0 = Not defined (The property is not observed when placing and replacing the symbol.)

1 = Yes (A function with signal isolation is generated for this symbol when placing and replacing the symbol.)

2 = No (A function without signal isolation is generated for this symbol when placing and replacing the symbol.)
