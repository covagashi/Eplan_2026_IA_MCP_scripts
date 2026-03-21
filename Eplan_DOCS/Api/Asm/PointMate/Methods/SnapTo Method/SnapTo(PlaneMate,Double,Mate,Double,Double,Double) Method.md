# SnapTo(PlaneMate,Double,Mate,Double,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate~SnapTo(PlaneMate,Double,Mate,Double,Double,Double).html

---

Snap this mate to another mate.

Syntax

**C#**



public void SnapTo( 

   PlaneMate pTargetMate,

   double dRotationAngle,

   Mate additionalTargetMate,

   double dXOffset,

   double dYOffset,

   double dZOffset

)

public:

void SnapTo( 

   PlaneMate^ pTargetMate,

   double dRotationAngle,

   Mate^ additionalTargetMate,

   double dXOffset,

   double dYOffset,

   double dZOffset

)


#### Parameters

*pTargetMate*
:   PlaneMato to snap to.

*dRotationAngle*
:   rotation angle (radian).

*additionalTargetMate*
:   additional mate to define x and y on the mate.

*dXOffset*


*dYOffset*


*dZOffset*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.SnappingFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SnappingFailedException.html) | Thrown when operation failed. Check exception message for more info. |

Remarks

Snapping means that the position and/or orientation of the associated placement will change, so that this mate fits to the target mate. Usually after the snapping, Placement3D becomes a child of the 'owner' of a target mate. There are however exceptions. For example when placing a component on a mounting point (like RP16) and in the same position there is a mounting surface, then component is arranged hierarchically below the mounting surface. If there is no mounting surface, then the component is arranged under cabinet.
