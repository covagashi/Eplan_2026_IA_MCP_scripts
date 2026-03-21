# AddSymbolPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPosition~AddSymbolPosition.html

---

Add a new symbol position to part. Symbol is added at the first available index of symbol position list.

Syntax

**C#**



public static MDSymbolPosition AddSymbolPosition( 

   MDPart pMDPart,

   string strSymbolLibraryName,

   int iSymbolNr,

   int iSymbolVariantNr

)

public:

static MDSymbolPosition^ AddSymbolPosition( 

   MDPart^ pMDPart,

   String^ strSymbolLibraryName,

   int iSymbolNr,

   int iSymbolVariantNr

)


#### Parameters

*pMDPart*
:   MDPart to which new symbol position will be added.

*strSymbolLibraryName*
:   Name of symbol library which stores the symbol. Can't be `null` or `empty`.

*iSymbolNr*
:   Number of the symbol.

*iSymbolVariantNr*
:   Variant index of the symbol.

#### Return Value

New created symbol position.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if `strSymbolLibraryName` is `null` or empty. |
| [MDCanNotAddSymbolPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDCanNotAddSymbolPosition.html) | Thrown when adding new symbol position has failed. |
