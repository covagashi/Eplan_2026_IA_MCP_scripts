# Parent Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Parent.html

---

Returns the symbol reference that the logical conn. point represented by this object belongs to.

Syntax

**C#**



public SymbolReference Parent {get;}

public:

property SymbolReference^ Parent {

   SymbolReference^ get();

}


Remarks

This property may return NULL if this PinBase object represents a symbol's graphical conn. point and the symbol is not instantiated in a project.
