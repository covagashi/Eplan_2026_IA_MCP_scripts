# VerifyPages(ArrayList,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyPages(ArrayList,String).html

---

Starts a check run for the given pages.

Syntax

**C#**



public void VerifyPages( 

   ArrayList colPages,

   string strVerificationScheme

)

public:

void VerifyPages( 

   ArrayList^ colPages,

   String^ strVerificationScheme

)


#### Parameters

*colPages*
:   List of pages to check.

*strVerificationScheme*
:   Scheme to use for the check run.

Exceptions

| Exception | Description |
| --- | --- |
| **InvalidScheme** | An error occurred when used scheme name doesn't exist |

Remarks

If the scheme name is empty, the last-used scheme will be used which is currently set in GUI.
