# CreateNewBendingPoint(Double,Double,Double,Plane,Double,BendingType) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic467.html

---

Creates new bending point on a plane of the bus bar

Syntax

**C#**



public Plane[] CreateNewBendingPoint( 

   double point,

   double pointSide,

   double angle,

   Plane plane,

   double bendingRadius,

   BusBar.Enums.BendingType bendingType

)

public:

array<Plane^>^ CreateNewBendingPoint( 

   double point,

   double pointSide,

   double angle,

   Plane^ plane,

   double bendingRadius,

   BusBar.Enums.BendingType bendingType

)


#### Parameters

*point*
:   Bending point position (from a plane beginning)

*pointSide*
:   Side point position (from a plane beginning)

*angle*
:   Angle in degrees

*plane*
:   Plane of the bus bar

*bendingRadius*
:   Bending radius. Must be greater then zero.

*bendingType*
:   Bending type

#### Return Value

New planes created with the new bending point (upper, lower, left and right) or a null if creation unsuccessful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if point coordinate exceeds length of a plane . |

Remarks

Please be aware that 'point' and 'pointSide' parameters is exactly X-coordinate in a plane coordinate system. It is visible when 'Activate directly' option is enabled on a plane
