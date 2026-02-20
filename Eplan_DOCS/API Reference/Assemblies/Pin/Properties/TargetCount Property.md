# TargetCount Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~TargetCount.html

---

Returns number of connections from this Pin object.

Syntax

**C#**



public int TargetCount {get;}

public:

property int TargetCount {

   int get();

}


Remarks

Returns `0` if this Pin object has been obtained from a FunctionDefinition object.
