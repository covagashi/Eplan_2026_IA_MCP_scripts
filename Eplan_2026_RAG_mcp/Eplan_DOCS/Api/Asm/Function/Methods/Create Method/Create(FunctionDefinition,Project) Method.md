# Create(FunctionDefinition,Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(FunctionDefinition,Project).html

---

Creates a not placed Function from [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) passed as parameter.

Syntax

**C#**



public static Function Create( 

   FunctionDefinition pFunctionDefinition,

   Project pProject

)

public:

static Function^ Create( 

   FunctionDefinition^ pFunctionDefinition,

   Project^ pProject

)


#### Parameters

*pFunctionDefinition*
:   [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) used to create the Function.

*pProject*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the Function will be located in.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |

Example

Example shows how to create function with help of function definition:

**C#**

```


//create function object based on function definition

Function oNewFunction = Function.Create(oFuncDef, oPage.Project);

//place created function on page

oNewFunction.Page = oPage;

```
