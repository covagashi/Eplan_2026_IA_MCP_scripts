# RemoveSymbolPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveSymbolPosition.html

---

Removes the given symbol position from the part.

Syntax

**C#**



public void RemoveSymbolPosition( 

   MDSymbolPosition pSymbolPosition

)

public:

void RemoveSymbolPosition( 

   MDSymbolPosition^ pSymbolPosition

)


#### Parameters

*pSymbolPosition*
:   MDSymbolPosition which will be removed. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if `pSymbolPosition` is `null`. |
