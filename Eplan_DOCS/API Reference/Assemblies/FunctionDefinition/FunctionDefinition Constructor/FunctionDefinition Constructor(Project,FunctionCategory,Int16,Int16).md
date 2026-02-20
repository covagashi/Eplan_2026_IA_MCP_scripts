# FunctionDefinition Constructor(Project,FunctionCategory,Int16,Int16)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~_ctor(Project,FunctionCategory,Int16,Int16).html

---

Constructs and initializes a FunctionDefinition object with the specified function's category, group and ID. Note: The specified function definition must exist in the project's standard function definitions library

Syntax

**C#**



public FunctionDefinition( 

   Project prj,

   FunctionCategory funcCategory,

   short funcGroup,

   short funcID

)

public:

FunctionDefinition( 

   Project^ prj,

   FunctionCategory funcCategory,

   short funcGroup,

   short funcID

)


#### Parameters

*prj*


*funcCategory*
:   Category of the function definition.

*funcGroup*
:   Group identifier of the function definition.

*funcID*
:   Identifier of the function definition.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the specified function definition (category, group and ID) doesn't exists in the project's function definitions library. |
