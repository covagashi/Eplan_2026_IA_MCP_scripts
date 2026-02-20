# Open(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Open(String).html

---

Opens an existing symbol library for exclusive access.

Syntax

**C#**



public static MDSymbolLibrary Open( 

   string strSymbolLibraryPath

)

public:

static MDSymbolLibrary^ Open( 

   String^ strSymbolLibraryPath

)


#### Parameters

*strSymbolLibraryPath*
:   filename of the library that will be opened

#### Return Value

symbol library that is opened

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when readonly database is opened in exclusive mode. |
