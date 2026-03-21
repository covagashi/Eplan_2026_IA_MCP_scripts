# Open Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Open(String,Project).html

---

Opens a macro file and retrieves infomation from it.

Syntax

**C#**



public void Open( 

   string macroFileName,

   Project oProject

)

public:

void Open( 

   String^ macroFileName,

   Project^ oProject

)


#### Parameters

*macroFileName*
:   Filename (inclusive path information and type) of the macro

*oProject*
:   the related project

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. p.e. a wrong filename. |
