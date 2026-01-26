# UnGroup(Placement,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~UnGroup(Placement,Boolean,Boolean).html

---

Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) only from a group.

Syntax

**C#**



public void UnGroup( 

   Placement placement,

   bool bRemoveEmptyGroup,

   bool bRedraw

)

public:

void UnGroup( 

   Placement^ placement,

   bool bRemoveEmptyGroup,

   bool bRedraw

)


#### Parameters

*placement*


*bRemoveEmptyGroup*
:   If true method will remove also Group when it becomes empty.

*bRedraw*
:   If true, GED is redrawn after the ungrouping.

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
