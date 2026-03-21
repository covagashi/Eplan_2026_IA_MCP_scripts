# GetPointAt Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PolyLine~GetPointAt.html

---

Returns the coordinates of a vertex of a polyline

Syntax

**C#**



public PointD GetPointAt( 

   int index

)

public:

PointD GetPointAt( 

   int index

)


#### Parameters

*index*
:   Index of the point to be determined. The index starts with 0.

#### Return Value

Coordinates of the point.

Remarks

The count of vertexes of a polyline can be determined by NumberOfPoints method.
