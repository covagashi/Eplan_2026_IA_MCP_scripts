# SetArea Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding~SetArea.html

---

Sets the size of a shielding using the coordinates of the two opposite corners

Syntax

**C#**



public void SetArea( 

   PointD pntStart,

   PointD pntEnd

)

public:

void SetArea( 

   PointD pntStart,

   PointD pntEnd

)


#### Parameters

*pntStart*
:   First corner of the shielding

*pntEnd*
:   Second corner of the shielding

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the area cannot be set. |
