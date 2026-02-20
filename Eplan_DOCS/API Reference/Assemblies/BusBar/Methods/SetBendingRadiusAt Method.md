# SetBendingRadiusAt Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~SetBendingRadiusAt.html

---

Sets bending radius at specific bending point

Syntax

**C#**



public void SetBendingRadiusAt( 

   double dNewRadius,

   long nBendingPoint

)

public:

void SetBendingRadiusAt( 

   double dNewRadius,

   int64 nBendingPoint

)


#### Parameters

*dNewRadius*
:   Radius.

*nBendingPoint*
:   Bending point (1,...,n-1).

Remarks

A bus bar with one angle has three bending points (0,1,2). Please be aware that the number of radiuses should be equal to number of bending points (ie. in .BendingPoints property) Otherwise, i.e if there could be an exception thrown or , if there are only 2, they are set to all the points.
