# CreateNewBendingPoint(Double,Double,Plane,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~CreateNewBendingPoint(Double,Double,Plane,Double).html

---

Creates new bending point on a plane of the bus bar

Syntax

**C#**



public Plane[] CreateNewBendingPoint( 

   double point,

   double angle,

   Plane plane,

   double bendingRadius

)

public:

array<Plane^>^ CreateNewBendingPoint( 

   double point,

   double angle,

   Plane^ plane,

   double bendingRadius

)


#### Parameters

*point*
:   Bending point position (from a plane beginning)

*angle*
:   Angle in degrees

*plane*
:   Plane of the bus bar

*bendingRadius*
:   Bending radius. Must be greater then zero.

#### Return Value

New planes created with the new bending point (upper, lower, left and right) or a null if creation unsuccessful. The bending type is flat.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if point coordinate exceeds length of a plane . |

Remarks

Please be aware that 'point' parameter is exactly X-coordinate in a plane coordinate system. It is visible when 'Activate directly' option is enabled on a plane. The rotated part starts from bending point and ends at a plane end. The method updated positions of items placed on the mounting surfaces (holes, etc)
