# Create(PLC,FunctionDefinition) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~Create(PLC,FunctionDefinition).html

---

Creates a Terminal object related to a [PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html) given as the parameter and having the specified function definition. The function definition must be of the 'PLC Terminal' category; otherwise a WrongCategoryException is thrown.

Syntax

**C#**



public void Create( 

   PLC plc,

   FunctionDefinition funcDef

)

public:

void Create( 

   PLC^ plc,

   FunctionDefinition^ funcDef

)


#### Parameters

*plc*
:   [PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html) where the Terminal will be located on

*funcDef*
:   The [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) that the Terminal will have assigned

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Terminal cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `plc` parameter is `null`. |
| [System.ArgumentNullException](#) | Thrown when `variant` parameter is `null`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the function has already been created. |
| [Eplan.EplApi.DataModel.WrongCategoryException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WrongCategoryException.html) | Thrown when the `funcDef` parameter does not point to a function definition of the 'PLC Terminal' category. |
