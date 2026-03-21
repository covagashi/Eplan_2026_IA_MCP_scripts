# TargetPins Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~TargetPins.html

---

Returns Pin objects of other functions connected directly with this conn. point.

Syntax

**C#**



public Pin[] TargetPins {get;}

public:

property array<Pin^>^ TargetPins {

   array<Pin^>^ get();

}


Remarks

Returns `NULL` if this Pin object has been obtained from a FunctionDefinition object.
