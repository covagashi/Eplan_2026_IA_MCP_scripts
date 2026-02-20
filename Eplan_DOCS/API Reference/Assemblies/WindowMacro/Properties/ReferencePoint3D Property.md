# ReferencePoint3D Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ReferencePoint3D.html

---

The position of user defined handle.

Syntax

**C#**



public PointD3D ReferencePoint3D {get;}

public:

property PointD3D ReferencePoint3D {

   PointD3D get();

}


#### Property Value

The reference point.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not be opened successfully. |

Remarks

Position of handle used for placing macro. Coordinates of this handle are defined in coordinate system of macro.
