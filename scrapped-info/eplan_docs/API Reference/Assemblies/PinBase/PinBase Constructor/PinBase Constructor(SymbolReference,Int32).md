# PinBase Constructor(SymbolReference,Int32)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~_ctor(SymbolReference,Int32).html

---

Creates a PinBase object representing a graphical connection point of a symbol and initializes Index, Parent, Direction and Location properties.

Syntax

**C#**



public PinBase( 

   SymbolReference smbl,

   int pinIdx

)

public:

PinBase( 

   SymbolReference^ smbl,

   int pinIdx

)


#### Parameters

*smbl*
:   SymbolReference object which gives a symbol variant for initialization of the Direction and Location properties. May be NULL.

*pinIdx*
:   Index of this connection point among the symbol's connection points.
