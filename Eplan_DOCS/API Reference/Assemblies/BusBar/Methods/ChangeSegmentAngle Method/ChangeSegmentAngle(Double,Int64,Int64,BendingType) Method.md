# ChangeSegmentAngle(Double,Int64,Int64,BendingType) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~ChangeSegmentAngle(Double,Int64,Int64,BendingType).html

---

Change angle between segments of bended bus bar.

Syntax

**C#**



public void ChangeSegmentAngle( 

   double dNewAngle,

   long nFixBendingPoint,

   long nMovingBendingPoint,

   BusBar.Enums.BendingType bendingType

)

public:

void ChangeSegmentAngle( 

   double dNewAngle,

   int64 nFixBendingPoint,

   int64 nMovingBendingPoint,

   BusBar.Enums.BendingType bendingType

)


#### Parameters

*dNewAngle*
:   Angle in radians.

*nFixBendingPoint*
:   Fix bending point (1,...,n-1).

*nMovingBendingPoint*
:   Moving bending point (Must be greater or less than fix bending point).

*bendingType*
:   Bending type

Remarks

A bus bar that is bent has at least three bending points (0,1,2).
