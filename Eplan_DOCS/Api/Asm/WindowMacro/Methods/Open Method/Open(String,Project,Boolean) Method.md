# Open(String,Project,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Open(String,Project,Boolean).html

---

Opens a macro file and reads the information. The first existing variant will be set as current variant

Syntax

**C#**



public void Open( 

   string macroFileName,

   Project oProject,

   bool bFromCache

)

public:

void Open( 

   String^ macroFileName,

   Project^ oProject,

   bool bFromCache

)


#### Parameters

*macroFileName*
:   Filename (including path information and type) of the macro

*oProject*
:   The related project. If null then current parts database is used.

*bFromCache*
:   Says if object should be created from cache

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. p.e. a wrong filename. |
