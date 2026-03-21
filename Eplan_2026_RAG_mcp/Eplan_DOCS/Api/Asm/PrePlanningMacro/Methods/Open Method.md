# Open Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PrePlanningMacro~Open.html

---

Opens a macro file and reads the information.

Syntax

**C#**



public void Open( 

   string strMacroFileName,

   Project oProject

)

public:

void Open( 

   String^ strMacroFileName,

   Project^ oProject

)


#### Parameters

*strMacroFileName*
:   Filename (inclusive path information and type) of the macro. Can't be `null`.

*oProject*
:   The related PrePlanning project. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. |
| [System.IO.FileNotFoundException](#) | Thrown when file does not exists. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro could not be opened successfully. |
