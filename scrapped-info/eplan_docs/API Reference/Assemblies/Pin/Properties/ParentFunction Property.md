# ParentFunction Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~ParentFunction.html

---

Returns a function that this connection point belongs to.

Syntax

**C#**



public Function ParentFunction {get;}

public:

property Function^ ParentFunction {

   Function^ get();

}


Remarks

Returns `NULL` if this Pin object has been obtained from a FunctionDefinition object.
