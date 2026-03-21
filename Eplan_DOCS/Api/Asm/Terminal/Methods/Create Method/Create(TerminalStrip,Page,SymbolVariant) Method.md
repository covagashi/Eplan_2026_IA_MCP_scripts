# Create(TerminalStrip,Page,SymbolVariant) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~Create(TerminalStrip,Page,SymbolVariant).html

---

Creates a Terminal object related to a [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) given as a parameter and having a **Eplan.EplApi.DataModel.Function.Category** equal to `TERMINAL`. Its graphical symbol is taken from a [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) given as the third parameter. The page where terminal will be placed is taken from the second `page` parameter. If NULL, an unplaced terminal will be created.

Syntax

**C#**



public void Create( 

   TerminalStrip ts,

   Page page,

   SymbolVariant variant

)

public:

void Create( 

   TerminalStrip^ ts,

   Page^ page,

   SymbolVariant^ variant

)


#### Parameters

*ts*
:   [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) where the Terminal will be located on

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where the Terminal will be placed. If page is NULL terminal won't be placed.

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
