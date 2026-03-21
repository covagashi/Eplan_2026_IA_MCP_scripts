# IsGroupValid Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~IsGroupValid.html

---

Returns true, if group is valid if not, the group should be dissolved

Syntax

**C#**



public virtual bool IsGroupValid()

public:

virtual bool IsGroupValid();


#### Return Value

True if group is Valid .

Remarks

This method doesn't make sense for class "SymbolVariant". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant".
