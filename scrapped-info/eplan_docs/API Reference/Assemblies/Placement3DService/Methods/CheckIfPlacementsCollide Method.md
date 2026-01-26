# CheckIfPlacementsCollide Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Placement3DService~CheckIfPlacementsCollide.html

---

Checks whether two 3d objects collides each other.

Syntax

**C#**



public bool CheckIfPlacementsCollide( 

   Placement3D pPlacementA,

   Placement3D pPlacementB,

   bool bConsiderMountingClearance,

   bool bExcludeAllowedCollisions

)

public:

bool CheckIfPlacementsCollide( 

   Placement3D^ pPlacementA,

   Placement3D^ pPlacementB,

   bool bConsiderMountingClearance,

   bool bExcludeAllowedCollisions

)


#### Parameters

*pPlacementA*
:   First of 3d placements used to check collision. Can't be `null`.

*pPlacementB*
:   Second of 3d placements used to check collision. Can't be `null`.

*bConsiderMountingClearance*
:   Use mounting clearances for checking collisions.

*bExcludeAllowedCollisions*
:   If true, collisions which are allowed are not reported.

#### Return Value

Returns `true` if a collision between two objects is found.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The functionality is not available. |

Remarks

Method checks whether two objects collides each other. This is done by checking if bounding boxes of these objects don't share common space and if they do then the check is done using their meshes.

In some cases collisions between two objects are allowed. This happens due to inaccuracy of some meshes and is acceptable for example in case of a terminal on a rail. Parameter `bExcludeAllowedCollisions` helps to control whether such collisions should be reported or not.

Many objects in layout space represents only logical instances without meshes. For example Cabinet or Plane are one of such objects. In this case, collision with these objects will not be reported.
