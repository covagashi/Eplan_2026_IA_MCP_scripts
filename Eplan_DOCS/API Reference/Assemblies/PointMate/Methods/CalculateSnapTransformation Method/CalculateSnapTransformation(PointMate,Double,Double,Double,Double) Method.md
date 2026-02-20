# CalculateSnapTransformation(PointMate,Double,Double,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic699.html

---

calculate a transformation matrix, that can be used to transform the associated placement into snap position that means, that the position and/or orientation of the associated placement will change, so that this mate fits to the target mate.

Syntax

**C#**



public Matrix3D CalculateSnapTransformation( 

   PointMate pTargetMate,

   double dRotationAngle,

   double dXOffset,

   double dYOffset,

   double dZOffset

)

public:

Matrix3D CalculateSnapTransformation( 

   PointMate^ pTargetMate,

   double dRotationAngle,

   double dXOffset,

   double dYOffset,

   double dZOffset

)


#### Parameters

*pTargetMate*
:   target for snapping.

*dRotationAngle*
:   rotation angle (radian).

*dXOffset*


*dYOffset*


*dZOffset*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.SnappingFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SnappingFailedException.html) | Thrown when operation failed. Check exception message for more info. |
