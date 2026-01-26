# EvaluateAndSetAllVisibleNames() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllVisibleNames().html

---

Evaluate the visible names from the full names for all placed functions and interruption points on page.

Syntax

**C#**



public bool EvaluateAndSetAllVisibleNames()

public:

bool EvaluateAndSetAllVisibleNames();


#### Return Value

Returns "true" if any name has changed, modifies only functions, which name has been changed

Exceptions

| Exception | Description |
| --- | --- |
| **ApplicationException** | When page is not set. |
