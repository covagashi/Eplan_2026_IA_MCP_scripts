# CreateTransient(Project,SymbolVariant) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CreateTransient(Project,SymbolVariant).html

---

Creates a Function. It is not placed on any [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). Its category is taken from [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html).

Syntax

**C#**



public void CreateTransient( 

   Project proj,

   SymbolVariant symbVariant

)

public:

void CreateTransient( 

   Project^ proj,

   SymbolVariant^ symbVariant

)


#### Parameters

*proj*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the Function will be located in

*symbVariant*
:   [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) the Function will be assigned

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `symbVariant` is `null`. |
| [IncorrectSymbolTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectSymbolTypeException.html) | Thrown when the function cannot be created. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the function has already been created. |

Remarks

This method no longer can create functions with category Shielding. The correct way to create Shield object is either use one of static Create methods or use a method on Shield class.
