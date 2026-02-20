# SetGraphics Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DynamicConnectionLine~SetGraphics.html

---

Sets graphic representation from 2 points.

Syntax

**C#**



public void SetGraphics( 

   PointD pnt1,

   PointD pnt2

)

public:

void SetGraphics( 

   PointD pnt1,

   PointD pnt2

)


#### Parameters

*pnt1*
:   First point of connection line.

*pnt2*
:   Second point of connection line.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when graphical representation of this DynamicConnectionLine cannot be set. |
