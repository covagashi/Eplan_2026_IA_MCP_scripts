# SetEllipse Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Arc~SetEllipse.html

---

Sets ellipse

Syntax

**C#**



public void SetEllipse( 

   PointD pntLocation,

   double crdRadiusX,

   double crdRadiusY,

   double nAngle

)

public:

void SetEllipse( 

   PointD pntLocation,

   double crdRadiusX,

   double crdRadiusY,

   double nAngle

)


#### Parameters

*pntLocation*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) the location of the ellipse

*crdRadiusX*
:   the X-radius of the ellipse

*crdRadiusY*
:   the Y-radius of the ellipse

*nAngle*
:   the angle of the ellipse

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the ellipse cannot be set. |
