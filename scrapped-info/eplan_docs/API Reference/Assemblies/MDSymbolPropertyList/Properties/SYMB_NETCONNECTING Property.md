# SYMB_NETCONNECTING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_NETCONNECTING().html

---

Net-connecting # 16043.

Syntax

**C#**



public MDPropertyValue SYMB_NETCONNECTING {get; set;}

public:

property MDPropertyValue^ SYMB_NETCONNECTING {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows whether a net-connecting function is created when placing and replacing a symbol. The visibility of the property depends on the type of symbol. The following values are possible:

0 = Not defined (the property is not observed when placing and replacing the symbol).

1 = Yes (a net-connecting function is generated for this symbol when placing and replacing the symbol).

2 = No (a function that does not connect nets is generated for this symbol when placing and replacing the symbol).
