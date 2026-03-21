# GetAllFunctionsWithSameName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.FunctionVerification~GetAllFunctionsWithSameName.html

---

Returns all functions of the project with the same name. Can be called within the Execute function.

Syntax

**C#**



public void GetAllFunctionsWithSameName( 

   Function oFunction,

   ref ArrayList colFunctions

)

public:

void GetAllFunctionsWithSameName( 

   Function^ oFunction,

   ArrayList^% colFunctions

)


#### Parameters

*oFunction*
:   The function based on which other functions with the same name are to be searched.

*colFunctions*
:   The list of results giving all functions with the same name.

Remarks

This function uses an internal buffer mechanism and is therefore very quick when called several times in a check routine.
