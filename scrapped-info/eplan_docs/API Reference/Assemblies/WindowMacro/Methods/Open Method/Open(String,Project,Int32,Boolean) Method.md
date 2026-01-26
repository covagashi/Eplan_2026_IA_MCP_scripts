# Open(String,Project,Int32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Open(String,Project,Int32,Boolean).html

---

Opens a macro file and reads the information. The first existing representation type will be set as current representation type

Syntax

**C#**



public void Open( 

   string macroFileName,

   Project oProject,

   int nVariant,

   bool bFromCache

)

public:

void Open( 

   String^ macroFileName,

   Project^ oProject,

   int nVariant,

   bool bFromCache

)


#### Parameters

*macroFileName*
:   Filename (including path information and type) of the macro

*oProject*
:   the related project. If null then current parts database is used.

*nVariant*


*bFromCache*
:   Says if object should be created from cache

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. p.e. a wrong filename or wrong variant. |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when representation type or variant not found |
