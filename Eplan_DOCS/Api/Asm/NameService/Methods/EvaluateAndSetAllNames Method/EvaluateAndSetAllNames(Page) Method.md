# EvaluateAndSetAllNames(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllNames(Page).html

---

Sets the page and evaluates the full name for all placed functions and interruption points on page by calling EvaluateName for all those objects.

Syntax

**C#**



public bool EvaluateAndSetAllNames( 

   Page pPage

)

public:

bool EvaluateAndSetAllNames( 

   Page^ pPage

)


#### Parameters

*pPage*
:   Page to set.

#### Return Value

Returns "true" if any name has changed, modifies only functions, which name has been changed.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
