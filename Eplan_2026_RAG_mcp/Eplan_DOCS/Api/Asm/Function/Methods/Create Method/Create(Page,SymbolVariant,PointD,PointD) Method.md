# Create(Page,SymbolVariant,PointD,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Page,SymbolVariant,PointD,PointD).html

---

Creates a `Function` object placed on a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) given as a parameter and sets it [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) together with `LogicalArea`.

Syntax

**C#**



public virtual void Create( 

   Page page,

   SymbolVariant oSymbolVariant,

   PointD oStartPoint,

   PointD oEndPoint

)

public:

virtual void Create( 

   Page^ page,

   SymbolVariant^ oSymbolVariant,

   PointD oStartPoint,

   PointD oEndPoint

)


#### Parameters

*page*
:   [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)Page where the Function will be located on.

*oSymbolVariant*
:   [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html)Symbol variant for this function.

*oStartPoint*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html)Lower left corner of function's logical area.

*oEndPoint*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html)Upper right corner of function's logical area.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `oPage` parameter is `null`. |
| [IncorrectSymbolTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectSymbolTypeException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `oSymbolVariant` parameter is `null`. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the function has already been created. |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |
| [CreatingConnectionDefinitionPointsFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CreatingConnectionDefinitionPointsFailedException.html) | Thrown when creating connection definition points fail. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |

Remarks

This method no longer can create functions with category Shielding. The correct way to create Shield object is either use one of static Create methods or use a method on Shield class.
