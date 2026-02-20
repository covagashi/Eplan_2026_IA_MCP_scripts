# AdjustFullName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~AdjustFullName.html

---

Evaluates for a given Function3D the full name from the visible name and sets that evaluated value at the function-object

Syntax

**C#**



public bool AdjustFullName( 

   IFunctionBase pFunctionBase

)

public:

bool AdjustFullName( 

   IFunctionBase^ pFunctionBase

)


#### Parameters

*pFunctionBase*
:   Function3D for which name is evaluated.

#### Return Value

Returns false, if the full name could not be evaluated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
