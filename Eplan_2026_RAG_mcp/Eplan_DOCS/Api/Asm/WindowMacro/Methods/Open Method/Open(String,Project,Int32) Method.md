# Open(String,Project,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Open(String,Project,Int32).html

---

Opens a macro file and reads the information. The first existing representation type will be set as current representation type

Syntax

**C#**



public void Open( 

   string macroFileName,

   Project oProject,

   int nVariant

)

public:

void Open( 

   String^ macroFileName,

   Project^ oProject,

   int nVariant

)


#### Parameters

*macroFileName*
:   Filename (including path information and type) of the macro

*oProject*
:   the related project. If null then current parts database is used.

*nVariant*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. p.e. a wrong filename or wrong variant. |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when representation type or variant not found |
