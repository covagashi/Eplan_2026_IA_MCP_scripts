# EvaluateAndSetAllNames() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllNames().html

---

Evaluates the full name for all placed functions and interruption points on page by calling EvaluateName for all those objects.

Syntax

**C#**



public bool EvaluateAndSetAllNames()

public:

bool EvaluateAndSetAllNames();


#### Return Value

Returns "true" if any name has changed, modifies only functions, which name has been changed.

Exceptions

| Exception | Description |
| --- | --- |
| **ApplicationException** | When page is not set. |
