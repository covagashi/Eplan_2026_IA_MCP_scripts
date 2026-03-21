# HasReferencePoint Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~HasReferencePoint.html

---

Returns true if a reference point has been defined for this macro.

Syntax

**C#**



public bool HasReferencePoint {get;}

public:

property bool HasReferencePoint {

   bool get();

}


#### Property Value

true : The macro file has a reference point defined.

false : The macro file has no reference point defined.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro could not be opened successfully. |
