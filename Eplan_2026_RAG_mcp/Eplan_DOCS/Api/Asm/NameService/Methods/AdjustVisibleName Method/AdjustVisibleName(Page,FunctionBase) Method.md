# AdjustVisibleName(Page,FunctionBase) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~AdjustVisibleName(Page,FunctionBase).html

---

Sets the page and evaluates for a given functionbase the visible name and visible name format from the fullname of the functionbase and sets these evaluated values at the functionbase-object

Syntax

**C#**



public bool AdjustVisibleName( 

   Page pPage,

   FunctionBase pFunctionBase

)

public:

bool AdjustVisibleName( 

   Page^ pPage,

   FunctionBase^ pFunctionBase

)


#### Parameters

*pPage*
:   Page to set.

*pFunctionBase*
:   Function for which the name is evaluated.

#### Return Value

Returns false, if the instance name could not be evaluated and set due to nesting.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
