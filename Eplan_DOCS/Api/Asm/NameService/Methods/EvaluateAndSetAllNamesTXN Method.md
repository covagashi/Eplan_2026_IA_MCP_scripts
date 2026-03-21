# EvaluateAndSetAllNamesTXN Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllNamesTXN.html

---

Evaluate all names for all FunctionBase objects in the project by calling EvaluateName for all those objects. This methods does own transactions, so no transactions around the method are allowed.

Syntax

**C#**



public void EvaluateAndSetAllNamesTXN( 

   Project pProject,

   bool bReEvaluateVisibleName,

   bool bReParseVisibleName

)

public:

void EvaluateAndSetAllNamesTXN( 

   Project^ pProject,

   bool bReEvaluateVisibleName,

   bool bReParseVisibleName

)


#### Parameters

*pProject*
:   Project for which names are evaluated.

*bReEvaluateVisibleName*
:   Whether evaluate visible name.

*bReParseVisibleName*
:   Whether parse visible name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
