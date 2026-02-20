# BreakUp() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~BreakUp().html

---

Breaks up the block into its individual elements.

Syntax

**C#**



public Placement[] BreakUp()

public:

array<Placement^>^ BreakUp();


#### Return Value

A [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) array.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when operation has failed. |

Remarks

If the block contains a SymbolReference object (which is the block reference itself), this object is also returned in the array (even if it is not considered when evaluating the Count property).
