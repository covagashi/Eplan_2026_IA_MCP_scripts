# SelectEplanVersion() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.EplanFinder~SelectEplanVersion().html

---

Select one EPLAN application installed on this machine. When there are more than one installed, a select dialog will appear.

Syntax

**C#**



public string SelectEplanVersion()

public:

String^ SelectEplanVersion();


#### Return Value

The EPLAN product variant bin path of the selected EPLAN application. Returns null if the user canceled.

Remarks

Selects a 32 bit installation only.
