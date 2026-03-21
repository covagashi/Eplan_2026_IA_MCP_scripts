# ChangeSegmentLength Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~ChangeSegmentLength.html

---

Change length of segment of bended bus bar.

Syntax

**C#**



public void ChangeSegmentLength( 

   double dNewLength,

   long nFixBendingPoint,

   long nMovingBendingPoint

)

public:

void ChangeSegmentLength( 

   double dNewLength,

   int64 nFixBendingPoint,

   int64 nMovingBendingPoint

)


#### Parameters

*dNewLength*
:   New length of segment between nFixBendingPoint and nMovingBendingPoint.

*nFixBendingPoint*
:   The marker of bending point that is fix (0,...,n) and will not move.

*nMovingBendingPoint*
:   The marker of moving bending point (must be greater or less than fix bending point)

Remarks

A bus bar with one angle has three bending points (0,1,2).  
Example calling:  
ChangeSegmentLength(200, 0, 1)  
will set length of first segment of bus bar to 200 when bending point marked as 0 stays motionless, while bending point marked as 1 is moving.  
ChangeSegmentLength(300, 1, 2)  
will set second segment of bended bus bar to 300 when point 1 stays motionless and point marked with 2 is moved.
