# Size Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Size.html

---

Returns the size of the macro. When available it is the size of the macro box, otherwise the graphical size (selection). If no selection was made when macro was created (for example via P8-API), it is a minimal size needed to contain all placements. If macro doesn't contain any placements, returned size is equal to (0,0).

Syntax

**C#**



public PointD Size {get;}

public:

property PointD Size {

   PointD get();

}


#### Property Value

the size of the macro

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not opened before or could not opened successfully. |
