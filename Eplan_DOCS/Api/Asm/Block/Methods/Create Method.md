# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~Create.html

---

Creates valid `Block` object from the passed elements. At least two elements must be passed in `arrPlacements`.

Syntax

**C#**



public void Create( 

   Page oPage,

   Placement[] arrPlacements

)

public:

void Create( 

   Page^ oPage,

   array<Placement^>^ arrPlacements

)


#### Parameters

*oPage*
:   Page on which the `block reference` will be placed. Can't be null.

*arrPlacements*
:   List of [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) which will be combined into a `block`. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when any parameter is `null`. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when page or one of placements is invalid, number of passed placements is less then two or more then one [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) object is in `arrParameters` |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the `block` cannot be created. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType set to ExternalDocument. |

Remarks

\* Only one [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) object can be passed in `arrPlacements`. In such a case that SymbolReference object becomes the block itself. \* If a new block is created and one of its elements is a symbol reference which already has some embedded objects (i.e. it is a block reference itself), new block is not created but rather the other elements are inserted to the already existing block. After such operation, two Block objects refer to the same block reference in the project. \* IMPORTANT: Graphical placements passed in the `arrPlacements` parameter become invalid (i.e. destroyed) after they are embedded into a block.
