# RepresentationTypes Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~RepresentationTypes.html

---

macro Representation Types.

Syntax

**C#**



public WindowMacro.Enums.RepresentationType[] RepresentationTypes {get;}

public:

property array<WindowMacro.Enums.RepresentationType>^ RepresentationTypes {

   array<WindowMacro.Enums.RepresentationType>^ get();

}


#### Property Value

a vector with all macro Representation Types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not opened before or could not opened successfully. |
