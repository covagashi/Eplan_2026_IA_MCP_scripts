# PlacementAreaTransformation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~PlacementAreaTransformation.html

---

Returns the transformation of macro placement area.

Syntax

**C#**



public Matrix3D PlacementAreaTransformation {get;}

public:

property Matrix3D PlacementAreaTransformation {

   Matrix3D get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not opened before or could not opened successfully. |

Remarks

This property represents relative to coordinate system of macro.
