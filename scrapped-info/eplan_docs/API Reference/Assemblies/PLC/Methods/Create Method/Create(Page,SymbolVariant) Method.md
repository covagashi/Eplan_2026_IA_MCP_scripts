# Create(Page,SymbolVariant) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC~Create(Page,SymbolVariant).html

---

Creates a SymbolReference. It is placed on the page passed as a parameter, using a given SymbolVariant.

Syntax

**C#**



public override void Create( 

   Page page,

   SymbolVariant variant

)

public:

void Create( 

   Page^ page,

   SymbolVariant^ variant

) override


#### Parameters

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where the symbol reference will be located on

*variant*
:   [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) representing the graphical symbol of the PLC

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `symbVariant` is `null`. |
| [IncorrectSymbolTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectSymbolTypeException.html) | Thrown when symbVariant is incompatible with this object. See [IncorrectSymbolTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectSymbolTypeException.html) for details. |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |

Remarks

This method no longer can create functions with category Shielding. The correct way to create Shield object is either use one of static Create methods or use a method on Shield class.
