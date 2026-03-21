# Create(String,Int32,Placement[],MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic745.html

---

Opens a macro file and reads the information.

Syntax

**C#**



public void Open( 

   string macroFileName,

   Project oProject,

   WindowMacro.Enums.RepresentationType nRepresentationType,

   int nVariant,

   bool bFromCache

)

public:

void Open( 

   String^ macroFileName,

   Project^ oProject,

   WindowMacro.Enums.RepresentationType nRepresentationType,

   int nVariant,

   bool bFromCache

)


#### Parameters

*macroFileName*
:   Filename (including path information and type) of the macro

*oProject*
:   the related project

*nRepresentationType*


*nVariant*


*bFromCache*
:   Says if object should be created from cache

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. p.e. a wrong filename. |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when representation type or variant not found |
