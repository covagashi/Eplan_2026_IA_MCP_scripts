# Move Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~Move.html

---

Moves the group

Syntax

**C#**



public void Move( 

   PointD pntMovement

)

public:

void Move( 

   PointD pntMovement

)


#### Parameters

*pntMovement*
:   Coordinates of moving vector

Remarks

The method moves whole group. Positions of sub-Placements in relation to the group location is the same as before. This method doesn't make sense for class "SymbolVariant". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant".
