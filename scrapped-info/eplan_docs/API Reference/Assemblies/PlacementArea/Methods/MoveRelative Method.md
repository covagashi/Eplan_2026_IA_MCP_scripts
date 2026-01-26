# MoveRelative Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlacementArea~MoveRelative.html

---

Moves placement area toward the axis of the normal vector of placement area.

Syntax

**C#**



public bool MoveRelative( 

   double dOffset

)

public:

bool MoveRelative( 

   double dOffset

)


#### Parameters

*dOffset*
:   The distance the object is moved. If negative the shift will be done in opposite direction.

#### Return Value

Returns `true` if operation was successful.
