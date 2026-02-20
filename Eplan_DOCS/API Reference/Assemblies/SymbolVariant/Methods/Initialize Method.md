# Initialize Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant~Initialize.html

---

Initializes the SymbolVariant object.

Syntax

**C#**



public void Initialize( 

   Symbol symbol,

   int variantNr

)

public:

void Initialize( 

   Symbol^ symbol,

   int variantNr

)


#### Parameters

*symbol*
:   [Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html) symbol that variant is created

*variantNr*
:   number of the variant of symbol

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `symbol` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the SymbolVariant cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the SymbolVariant has already been created. |
