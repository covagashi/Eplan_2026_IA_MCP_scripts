# AdjustFullName(FunctionBase) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~AdjustFullName(FunctionBase).html

---

Evaluates for a given functionbase the full name from the visible name of the functionbase and sets that evaluated value at the functionbase-object

Syntax

**C#**



public bool AdjustFullName( 

   FunctionBase pFunctionBase

)

public:

bool AdjustFullName( 

   FunctionBase^ pFunctionBase

)


#### Parameters

*pFunctionBase*
:   Function for which is evaluated name.

#### Return Value

Returns false, if the full name could not be evaluated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | When page is not set. |
