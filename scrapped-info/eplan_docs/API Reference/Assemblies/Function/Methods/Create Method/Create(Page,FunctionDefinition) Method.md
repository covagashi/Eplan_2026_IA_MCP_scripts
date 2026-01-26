# Create(Page,FunctionDefinition) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Page,FunctionDefinition).html

---

Creates a Function object placed on a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) given as the first parameter and having a [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) taken from [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) passed as the second parameter.

Syntax

**C#**



public void Create( 

   Page page,

   FunctionDefinition functionDefinition

)

public:

void Create( 

   Page^ page,

   FunctionDefinition^ functionDefinition

)


#### Parameters

*page*
:   [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) where the Function will be placed on

*functionDefinition*
:   [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) the Function will be assigned

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `functionDefinition` is `null`. |
| [IncorrectSymbolTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectSymbolTypeException.html) | Thrown when the function cannot be created. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the function has already been created. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |

Remarks

This method no longer can create functions with category Shielding. The correct way to create Shield object is either use one of static Create methods or use a method on Shield class.
