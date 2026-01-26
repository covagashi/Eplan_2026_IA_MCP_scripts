# DeepUnGroup() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~DeepUnGroup().html

---

Remove all [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group and it's sub groups.

Syntax

**C#**



public void DeepUnGroup()

public:

void DeepUnGroup();


Remarks

This method don't remove SubGroups. This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
