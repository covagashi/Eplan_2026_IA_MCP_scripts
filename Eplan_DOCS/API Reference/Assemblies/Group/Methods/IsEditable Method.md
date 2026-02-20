# IsEditable Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~IsEditable.html

---

Check if the Group is editable.

Syntax

**C#**



public bool IsEditable()

public:

bool IsEditable();


#### Return Value

True if group is editable .

Remarks

This method doesn't make sense for class "SymbolVariant". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant".
