# SetArea Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode~SetArea.html

---

Sets the size of a rectangle using the coordinates of the two opposite corners

Syntax

**C#**



public override void SetArea( 

   PointD pntStart,

   PointD pntEnd

)

public:

void SetArea( 

   PointD pntStart,

   PointD pntEnd

) override


#### Parameters

*pntStart*
:   First corner of the rectangle

*pntEnd*
:   Second corner of the rectangle

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the area cannot be set. |

Remarks

QRCode should always have equal value on height and width. This means that setting points to have other ratio than equal will throw exception.
