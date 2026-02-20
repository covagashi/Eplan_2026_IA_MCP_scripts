# RemoveSubPlacements(Placement[],Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacements(Placement[],Boolean).html

---

Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s from the group and from the project. The Placement objects passed into this method are no longer valid.

Syntax

**C#**



public virtual void RemoveSubPlacements( 

   Placement[] placements,

   bool bRemoveEmptyGroup

)

public:

virtual void RemoveSubPlacements( 

   array<Placement^>^ placements,

   bool bRemoveEmptyGroup

)


#### Parameters

*placements*


*bRemoveEmptyGroup*
:   If true method will remove also Group when it becomes empty.

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
