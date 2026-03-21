# Open(String,Mode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Open(String,Mode).html

---

Opens an existing symbol library.

Syntax

**C#**



public static MDSymbolLibrary Open( 

   string strSymbolLibraryPath,

   MDSymbolLibrary.Mode eMode

)

public:

static MDSymbolLibrary^ Open( 

   String^ strSymbolLibraryPath,

   MDSymbolLibrary.Mode eMode

)


#### Parameters

*strSymbolLibraryPath*
:   filename of the library that will be opened

*eMode*
:   mode of Open method

#### Return Value

symbol library that is opened

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when readonly database is opened in exclusive mode. |
