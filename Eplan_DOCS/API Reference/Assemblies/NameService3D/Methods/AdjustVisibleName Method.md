# AdjustVisibleName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~AdjustVisibleName.html

---

Evaluates for a given Function3D the visible name and visible name format from the fullname of the function and sets these evaluated values at the function-object

Syntax

**C#**



public bool AdjustVisibleName( 

   IFunctionBase pFunctionBase

)

public:

bool AdjustVisibleName( 

   IFunctionBase^ pFunctionBase

)


#### Parameters

*pFunctionBase*
:   Function3D for which the name is evaluated.

#### Return Value

Returns false, if the instance name could not be evaluated and set due to nesting.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
