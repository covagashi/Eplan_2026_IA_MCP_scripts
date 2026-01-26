# RemoveSubPlacement(Placement,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacement(Placement,Boolean).html

---

Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) from the group and from the project. The Placement object passed into this method is no longer valid.

Syntax

**C#**



public virtual void RemoveSubPlacement( 

   Placement placement,

   bool bRemoveEmptyGroup

)

public:

virtual void RemoveSubPlacement( 

   Placement^ placement,

   bool bRemoveEmptyGroup

)


#### Parameters

*placement*


*bRemoveEmptyGroup*
:   If true, the Group object will be removed also when it becomes empty.

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
