# Create(Project,FunctionDefinition) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Project,FunctionDefinition).html

---

Creates a Function. It is not placed on any [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). and having a [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) taken from [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) passed as the second parameter.

Syntax

**C#**



public void Create( 

   Project proj,

   FunctionDefinition functionDefinition

)

public:

void Create( 

   Project^ proj,

   FunctionDefinition^ functionDefinition

)


#### Parameters

*proj*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the Function will be located in

*functionDefinition*
:   [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) the Function will be assigned

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
