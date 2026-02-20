# SnapTo(PointMate,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate~SnapTo(PointMate,Double).html

---

Snap the mate to another point mate.

Syntax

**C#**



public void SnapTo( 

   PointMate pTargetMate,

   double dRotationAngle

)

public:

void SnapTo( 

   PointMate^ pTargetMate,

   double dRotationAngle

)


#### Parameters

*pTargetMate*
:   Target point mate for snapping.

*dRotationAngle*
:   Rotation angle (in radians).

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.SnappingFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SnappingFailedException.html) | Thrown when operation failed. Check exception message for more info. |

Remarks

Snapping means that the position and/or orientation of the associated placement will change, so that this mate fits to the target mate. Usually after the snapping, Placement3D becomes a child of the 'owner' of a target mate. There are however exceptions. For example when placing a component on a mounting point (like RP16) and in the same position there is a mounting surface, then component is arranged hierarchically below the mounting surface. If there is no mounting surface, then the component is arranged under cabinet.
