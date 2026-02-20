# Initialize(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary~Initialize(String).html

---

Opens a symbol library from system masterdata pool. Note: if this method returns true, it means that the library was actually open during the initialization and it is the client responsibility to close it.

Syntax

**C#**



public bool Initialize( 

   string libraryName

)

public:

bool Initialize( 

   String^ libraryName

)


#### Parameters

*libraryName*
:   Library name

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.SymbolLibraryOpeningFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolLibraryOpeningFailedException.html) | Opening symbol library failed |
