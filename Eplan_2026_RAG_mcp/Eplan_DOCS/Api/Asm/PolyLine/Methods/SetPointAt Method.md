# SetPointAt Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PolyLine~SetPointAt.html

---

Sets one vertex of a polyline If the index of this point does not yet exist it will be added.

Syntax

**C#**



public void SetPointAt( 

   int index,

   ref PointD point

)

public:

void SetPointAt( 

   int index,

   PointD% point

)


#### Parameters

*index*
:   Index of the point. The index starts with 0.

*point*
:   Coordinates of the point.
