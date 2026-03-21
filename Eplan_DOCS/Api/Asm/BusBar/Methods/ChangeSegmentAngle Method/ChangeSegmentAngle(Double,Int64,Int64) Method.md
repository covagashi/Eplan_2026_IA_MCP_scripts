# ChangeSegmentAngle(Double,Int64,Int64) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~ChangeSegmentAngle(Double,Int64,Int64).html

---

Change angle between segments of bended bus bar.

Syntax

**C#**



public void ChangeSegmentAngle( 

   double dNewAngle,

   long nFixBendingPoint,

   long nMovingBendingPoint

)

public:

void ChangeSegmentAngle( 

   double dNewAngle,

   int64 nFixBendingPoint,

   int64 nMovingBendingPoint

)


#### Parameters

*dNewAngle*
:   Angle in radians.

*nFixBendingPoint*
:   Fix bending point (1,...,n-1).

*nMovingBendingPoint*
:   Moving bending point (Must be greater or less than fix bending point).

Remarks

A bus bar with one angle has three bending points (0,1,2).
