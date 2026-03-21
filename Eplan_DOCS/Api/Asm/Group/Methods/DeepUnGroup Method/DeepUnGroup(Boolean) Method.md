# DeepUnGroup(Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~DeepUnGroup(Boolean).html

---

Remove all [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group and it's sub groups. If true method will remove also SubGroups.

Syntax

**C#**



public void DeepUnGroup( 

   bool bRemoveSubGroups

)

public:

void DeepUnGroup( 

   bool bRemoveSubGroups

)


#### Parameters

*bRemoveSubGroups*
:   If true method will remove also SubGroups.

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
