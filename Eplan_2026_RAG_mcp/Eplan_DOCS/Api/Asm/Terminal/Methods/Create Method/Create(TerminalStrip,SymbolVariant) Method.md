# Create(TerminalStrip,SymbolVariant) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~Create(TerminalStrip,SymbolVariant).html

---

Creates a Terminal object related to a [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) given as a parameter and having a **Eplan.EplApi.DataModel.Function.Category** equal to `TERMINAL`. Its graphical symbol is taken from a [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) given as the second parameter.

Syntax

**C#**



public void Create( 

   TerminalStrip ts,

   SymbolVariant variant

)

public:

void Create( 

   TerminalStrip^ ts,

   SymbolVariant^ variant

)


#### Parameters

*ts*
:   [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) where the Terminal will be located on

*variant*
:   [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) representing the graphical symbol of the terminal

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Terminal cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `ts` parameter is `null`. |
| [System.ArgumentNullException](#) | Thrown when `variant` parameter is `null`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the function has already been created. |
| [Eplan.EplApi.DataModel.WrongCategoryException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WrongCategoryException.html) | Thrown when the `variant` does not represent a Terminal. |
