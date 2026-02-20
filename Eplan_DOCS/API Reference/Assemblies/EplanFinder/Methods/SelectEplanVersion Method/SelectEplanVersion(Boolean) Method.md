# SelectEplanVersion(Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.EplanFinder~SelectEplanVersion(Boolean).html

---

Select one EPLAN application installed on this machine. When there are more than one installed, a select dialog will appear.

Syntax

**C#**



public string SelectEplanVersion( 

   bool b64bit

)

public:

String^ SelectEplanVersion( 

   bool b64bit

)


#### Parameters

*b64bit*
:   Select a 64 bit installation

#### Return Value

The EPLAN product variant bin path of the selected EPLAN application. Returns null if the user canceled.
