# SymbolConnPoint Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~SymbolConnPoint.html

---

Gets/Sets the underlying symbol's connection point assigned to this pin or `null`.

Syntax

**C#**



public PinBase SymbolConnPoint {get; set;}

public:

property PinBase^ SymbolConnPoint {

   PinBase^ get();

   void set (    PinBase^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `the index of the symbol's connection point being assigned` is greater than this pin's ParentFunction.SymbolVariant.ConnectionPoints.Length. |

Remarks

In most cases the PinBase object returned by this property will have its index equal to the pin's index - - this means 1:1 mapping of the symbol's connection points to the function's connection points. This property makes it possible to modify the mapping (i.e. assign different symbol's connection point to this pin).
