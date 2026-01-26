# EvaluateAndSetAllVisibleNames Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~EvaluateAndSetAllVisibleNames.html

---

Evaluate the visible names from the full names for all placed 3D functions in installation space.

Syntax

**C#**



public bool EvaluateAndSetAllVisibleNames()

public:

bool EvaluateAndSetAllVisibleNames();


#### Return Value

Returns "true" if any name has changed, modifies only functions, which name has been changed. The method uses only an installation space that was set in the constructor.
