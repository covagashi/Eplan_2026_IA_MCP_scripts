# Open(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Open(String).html

---

Opens a macro file using current parts database.

Syntax

**C#**



public void Open( 

   string macroFileName

)

public:

void Open( 

   String^ macroFileName

)


#### Parameters

*macroFileName*
:   Filename (including path information and type) of the macro

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. p.e. a wrong filename. |
