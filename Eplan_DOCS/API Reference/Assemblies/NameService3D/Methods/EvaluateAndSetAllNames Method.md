# EvaluateAndSetAllNames Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~EvaluateAndSetAllNames.html

---

Evaluates the full name for all placed 3D functions in installation space by calling EvaluateName for all those objects.

Syntax

**C#**



public bool EvaluateAndSetAllNames()

public:

bool EvaluateAndSetAllNames();


#### Return Value

Returns "true" if any name has changed, modifies only functions, which name has been changed. The method uses only an installation space that was set in the constructor.
