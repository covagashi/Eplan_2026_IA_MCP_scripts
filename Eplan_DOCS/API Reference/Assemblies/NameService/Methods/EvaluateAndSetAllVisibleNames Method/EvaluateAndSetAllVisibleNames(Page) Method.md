# EvaluateAndSetAllVisibleNames(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllVisibleNames(Page).html

---

Sets the page and evaluate the visible names from the full names for all placed functions and interruption points on page.

Syntax

**C#**



public bool EvaluateAndSetAllVisibleNames( 

   Page pPage

)

public:

bool EvaluateAndSetAllVisibleNames( 

   Page^ pPage

)


#### Parameters

*pPage*
:   Page to set.

#### Return Value

Returns "true" if any name has changed, modifies only functions, which name has been changed

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
