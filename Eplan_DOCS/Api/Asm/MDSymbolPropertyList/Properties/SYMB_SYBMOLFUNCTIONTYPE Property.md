# SYMB_SYBMOLFUNCTIONTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_SYBMOLFUNCTIONTYPE().html

---

Symbol representation type (encoded) # 16027.

Syntax

**C#**



public MDPropertyValue SYMB_SYBMOLFUNCTIONTYPE {get; set;}

public:

property MDPropertyValue^ SYMB_SYBMOLFUNCTIONTYPE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows in coded form the representation type of the symbol:

1 = Multi-line

2 = Single-line

38 = P&I diagram

-2 = Pair cross-reference

3 = Overview

-3 = External

5 = Graphic

8 = Panel layout

-6 = Detailed panel layout.
