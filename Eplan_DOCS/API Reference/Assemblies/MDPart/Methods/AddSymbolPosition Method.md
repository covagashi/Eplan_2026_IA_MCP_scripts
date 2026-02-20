# AddSymbolPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddSymbolPosition.html

---

Add a new symbol position to the part. Symbol is added at the first available index of symbol position list.

Syntax

**C#**



public MDSymbolPosition AddSymbolPosition( 

   string strSymbolLibraryName,

   int iSymbolNr,

   int iSymbolVariantId

)

public:

MDSymbolPosition^ AddSymbolPosition( 

   String^ strSymbolLibraryName,

   int iSymbolNr,

   int iSymbolVariantId

)


#### Parameters

*strSymbolLibraryName*
:   Name of symbol library which stores the symbol. Can't be `null` or `empty`.

*iSymbolNr*
:   Number of the symbol.

*iSymbolVariantId*
:   Variant index of the symbol.

#### Return Value

New created symbol position.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if `strSymbolLibraryName` is `null` or empty. |
| [MDCanNotAddSymbolPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDCanNotAddSymbolPosition.html) | Thrown when adding new symbol position has failed. |
