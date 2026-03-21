# ReferencePoint Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ReferencePoint.html

---

The reference point of the macro defined by the user when storing it.

Syntax

**C#**



public PointD ReferencePoint {get; set;}

public:

property PointD ReferencePoint {

   PointD get();

   void set (    PointD value);

}


#### Property Value

The reference point.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro it.could not be opened successfully. |

Remarks

To calculate relative coordinates of the reference point use `Location`.
