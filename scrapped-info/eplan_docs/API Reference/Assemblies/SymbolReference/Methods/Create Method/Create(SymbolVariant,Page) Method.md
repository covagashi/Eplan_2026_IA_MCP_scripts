# Create(SymbolVariant,Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Create(SymbolVariant,Page).html

---

Creates a SymbolReference or more specialized object derived from it, depending on symbol type and function definition assigned to the symbol in symbVariant parameter. The object is placed on the page passed as a parameter, using a given SymbolVariant.

Syntax

**C#**



public static SymbolReference Create( 

   SymbolVariant symbVariant,

   Page page

)

public:

static SymbolReference^ Create( 

   SymbolVariant^ symbVariant,

   Page^ page

)


#### Parameters

*symbVariant*
:   [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) that will be assigned

*page*
:   [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where the symbol reference will be located on

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `symbVariant` is `null`. |
| [IncorrectSymbolTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectSymbolTypeException.html) | Thrown when symbVariant is incompatible with this object. See [IncorrectSymbolTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectSymbolTypeException.html) for details. |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
