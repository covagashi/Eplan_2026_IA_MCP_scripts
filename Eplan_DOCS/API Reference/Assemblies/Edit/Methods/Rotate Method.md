# Rotate Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~Rotate.html

---

Rotates objects.

Syntax

**C#**



public void Rotate( 

   Placement[] plcmnts,

   PointD oPntStart,

   double angle

)

public:

void Rotate( 

   array<Placement^>^ plcmnts,

   PointD oPntStart,

   double angle

)


#### Parameters

*plcmnts*
:   Placements to rotate. All placements have to be placed on the same page.

*oPntStart*
:   Starting point for rotation

*angle*
:   Angle (in radians)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
| [System.ArgumentException](#) | Thrown when collection `plcmnts` contains objects with different or `NULL` parent. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when there are preplanning objects on preplanning page which could not be rotated or internal error occured. |

Remarks

Both graphical and logical elements may be rotated, however, when `plcmnts` contains any logical objects it could be rotated only in 90° increments. When different value in `angle` is given the rotation will align with the closest angle possible that is coherent with the rule.
