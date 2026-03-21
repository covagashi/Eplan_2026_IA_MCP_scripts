# Initialize(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary~Initialize(Project,String).html

---

Opens a symbol library of the project.

Syntax

**C#**



public void Initialize( 

   Project proj,

   string libraryName

)

public:

void Initialize( 

   Project^ proj,

   String^ libraryName

)


#### Parameters

*proj*
:   Project

*libraryName*
:   Library name

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.SymbolLibraryOpeningFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolLibraryOpeningFailedException.html) | Opening symbol library failed |
